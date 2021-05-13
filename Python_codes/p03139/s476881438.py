N, A, B = [int(i) for i in input().split()]

X = A if A < B else B
Y = 0 if N > A+B else A+B-N

print("{0} {1}".format(X, Y))