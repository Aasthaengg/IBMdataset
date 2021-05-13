N, M = map(int, input().split())
print((N-2 if N >= 2 else 1) * (M-2 if M >= 2 else 1))