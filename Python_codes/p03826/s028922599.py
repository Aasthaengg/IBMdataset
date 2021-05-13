a, b, c, d = map(int, input().split())

S1 = a * b
S2 = c * d

print(S1 if S1 > S2 else S2)
