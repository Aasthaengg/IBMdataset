n = int(input())
ab = [input().split() for _ in [0]*n]
a = [int(i) for i, j in ab][::-1]
b = [int(j) for i, j in ab][::-1]
ans = 0
for i in range(n):
    a[i] += ans
    if a[i] % b[i] != 0:
        ans += b[i] - (a[i] % b[i])
print(ans)
