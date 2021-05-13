A, B = map(int, input().split())

ans = max(A+B, A-B)
print(max(ans, A*B))
