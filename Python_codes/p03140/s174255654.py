input()
A, B, C = input(), input(), input()
print(sum([len(set([a, b, c])) - 1 for a, b, c in zip(A, B, C)]))
