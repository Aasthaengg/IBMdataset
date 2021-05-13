import sys
n,x = map(int, sys.stdin.readline().rstrip("\n").split())
a = [int(s) for s in sys.stdin.readline().rstrip("\n").split()]
a.sort()
ans = 0
for i in range(n):
    if i == n-1:
        if x - a[i] == 0:
            ans += 1
    else:
        if x-a[i] >= 0:
            x = x-a[i]
            ans += 1
print(ans)