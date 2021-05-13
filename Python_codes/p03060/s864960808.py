n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
xy = [0]*n
ans = 0
for i in range(n):
    xy[i] = v[i] - c[i]
    if xy[i] > 0:
        ans += xy[i]
print(ans)