S, T = input().split()
A, B = map(int, input().split())
U = input()
print(A-1 if S==U else A)
print(B if S==U else B-1)