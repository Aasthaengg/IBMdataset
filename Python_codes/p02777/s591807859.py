S, T = input().split()
A, B = map(int, input().split())
U = input()
print(A-1 if S == U else A, B-1 if T == U else B)