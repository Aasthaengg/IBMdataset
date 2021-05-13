N, A, B = map(int, input().split())

ans_min = B + A * (N - 1)
ans_max = B * (N - 1) + A

ans = max(0, ans_max - ans_min + 1)

print(ans)