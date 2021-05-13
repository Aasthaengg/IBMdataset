
A, B, C = map(int, input().split())
total = A*B*C
if A >= B and A >= C:
    x = A
    y = B
    z = C
elif B >= A and B >= C:
    x = B
    y = A
    z = C
else:
    x = C
    y = A
    z = B
if x % 2 == 0:
    ans = 0
else:
    ans = x % 2*y*z
print(ans)
