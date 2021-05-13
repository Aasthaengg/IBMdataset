import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
m = 0
for i in range(n):
    if a[i]<m:
        print("No")
        break
    m = max(m, a[i]-1)
else:
    print("Yes")