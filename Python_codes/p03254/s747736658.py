import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,x = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
s = 0
for i in range(n):
    if s+a[i]==x or (i<n-1 and s+a[i]<=x):
        s += a[i]
#         print(s)
    else:
        i -= 1
        break
print(i+1)