A, B, C, K = map(int, input().split())
ans = A - B
if K % 2 == 1 : ans = -ans
print(ans)