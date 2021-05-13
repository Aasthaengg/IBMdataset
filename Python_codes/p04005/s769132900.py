A, B, C = map(int, input().split())
mx = max(A, B, C)

if mx == B:
    A, B = B, A
elif mx == C:
    A, C = C, A

print(B*C*(A % 2))