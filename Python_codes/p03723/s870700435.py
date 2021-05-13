## A - Cookie Exchanges
A, B, C = map(int, input().split())
if not (A%2 == B%2 == C%2 == 0):
    ans = 0
elif A == B == C:
    ans = -1
else:
    ans = 0
    while A%2 == B%2 == C%2 == 0:
        a = (B+C) // 2
        b = (C+A) // 2
        c = (A+B) // 2
        A = a
        B = b
        C = c
        ans += 1
print(ans)

