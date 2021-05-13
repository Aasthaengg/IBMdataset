A, B, C = map(int, input().split())
if A%2 == B%2 == C%2 == 1:
    print(min(A*B, B*C, A*C))
else:
    print(0)