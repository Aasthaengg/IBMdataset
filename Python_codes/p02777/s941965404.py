S, T = input().split()
A, B = map(int, input().split())
U = input()

print(A - (S == U), B - (T == U))