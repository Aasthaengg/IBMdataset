N,M,X = map(int, input().split())
A = [int(i) for i in input().split()]

B = [i for i in A if i < X]
C = [i for i in A if i > X]

print( min(len(B), len(C)))
