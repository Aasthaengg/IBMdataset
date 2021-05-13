A, B, C, K = map(int, input().split())
ans = abs(A) - abs(B)
if K % 2 != 0:
    ans = ans * -1
print(ans)