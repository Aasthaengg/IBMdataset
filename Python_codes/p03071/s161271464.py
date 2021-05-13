A, B = map(int, input().split())
ans = max(max(A, B) * 2 - 1, A + B)
print(ans)