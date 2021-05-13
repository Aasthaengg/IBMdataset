N, A, B = map(int, input().split())
ans = (B-A)*(N-2) + 1
ans = max(0, ans)
print(ans)