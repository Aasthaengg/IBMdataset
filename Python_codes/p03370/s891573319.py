N, X = map(int, input().split())
M = [int(input()) for i in range(N)]
M_sum = sum(M)
M_min = min(M)
ans = N
ans += (X - M_sum) // M_min
print(ans)
