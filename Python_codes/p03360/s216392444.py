A, B, C = map(int, input().split())
K = int(input())

m = max(A, B, C)
m *= 2**K

ans = A + B + C - max(A, B, C)
ans += m
print(ans)
