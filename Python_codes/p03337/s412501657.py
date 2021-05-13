A, B = map(int, input().split())
ans = max(A + B, A - B)
ans = max(ans, A * B)

print(ans)