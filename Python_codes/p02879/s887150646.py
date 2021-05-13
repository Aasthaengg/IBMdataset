A, B = [int(s) for s in input().split(' ')]
a = 0 if A > 9 else A
b = 0 if B > 9 else B
print(a * b if a * b else -1)

