A, B, C = map(int, input().split())
x = max(A, B, C)
y = min(A, B, C)
z = A+B+C-(x+y)
if x % 2 == 0:
    ans = 0
else:
    ans = y*z
print(ans)
