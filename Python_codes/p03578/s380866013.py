import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
d.sort()
t.sort()
j = 0
for i in range(m):
    while j<n and d[j]<t[i]:
        j += 1
    if j>=n or d[j]!=t[i]:
        print("NO")
        break
    else:
        j += 1
else:
    print("YES")