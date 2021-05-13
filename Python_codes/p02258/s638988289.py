n = int(input())
R = list()

for _ in range(n):
    R.append(int(input()))

ans = R[1] - R[0]
min_R = R[0]

for i in range(1, n):
    ans   = max(ans, R[i] - min_R)
    min_R = min(min_R, R[i])
print(ans)