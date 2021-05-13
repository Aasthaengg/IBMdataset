A, B, C = map(int, input().split())
ans = 10**18

if A%2==0:
    ans = 0
else:
    ans = min(ans, B*C)

if B%2==0:
    ans = 0
else:
    ans = min(ans, C*A)

if C%2==0:
    ans = 0
else:
    ans = min(ans, A*B)

print(ans)