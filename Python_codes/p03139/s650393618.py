N, A, B = map(int, input().split())
ans_max = min(A, B)
ans_min = max(-(N - A - B), 0)
print(ans_max,ans_min)
