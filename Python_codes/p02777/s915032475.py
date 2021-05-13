S, T = input().split()
A, B = [int(s) for s in input().split()]
U = input()

print(A - (S == U), B - (T == U))
