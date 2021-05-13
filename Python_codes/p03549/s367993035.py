N, M = map(int, input().split())

v1 = (N - M) * 100
v2 = 1900 * M
v = v1 + v2
ans = v * pow(2, M)
print(ans)
