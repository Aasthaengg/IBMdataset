A, B, C = map(int, input().split())
ans = 0
if A * B * C % 2 != 0:
    ans = min((A * B), (A * C), (B * C))
print(ans)