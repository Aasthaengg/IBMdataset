A, B, C = map(int, input().split())

if A%2 == 0 and A == B and A == C:
    print(-1)
else:
    N = 0
    while A%2 == B%2 == C%2 == 0:
         N += 1
         A, B, C = (B + C)/2, (C + A)/2, (A + B)/2
    print(N)
