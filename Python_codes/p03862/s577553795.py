import sys
input = sys.stdin.readline
n,x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(1,n):
    if a[i-1] + a[i] > x:
        s = a[i-1] + a[i] - x
        if a[i] - s >= 0:
            a[i] -= s
            ans += s
        else:
            a[i] = 0
            ans += s
print(ans)
