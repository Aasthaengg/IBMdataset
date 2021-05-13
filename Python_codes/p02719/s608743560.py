N, K = map(int, input().split())

ans = 0

ans_1 = N//K
ans_2 = ans_1 + 1

ans = min(abs(N-ans_1*K), abs(N-ans_2*K))
print(ans)