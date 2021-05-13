A, B, C = map(int, input().split())
m = max(A, B, C)
s = A + B + C
if s % 2 == 3 * m % 2:
    ans = (3 * m - s) // 2
else:
    ans = (3 * (m + 1) - s) // 2
print(ans)
