A, B, C, K = map(int, input().split())
if 0 <= K <= A:
    ans = K
elif A + 1 <= K <= A + B:
    ans = A
else:
    ans = A - (K - A - B)
print(ans)
