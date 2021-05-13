N, A, B = map(int, input().split())

X = N//(A+B)
Y = N % (A+B)

print(X*A+min(A, Y))