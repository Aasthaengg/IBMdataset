S = list(map(int, input()))

A = S.count(0)
B = len(S) - A

print(min(A, B) * 2)