X, A, B = map(int, input().split())

a = A * (-1)

if (a+B < X+1) and (A < B):
    print("safe")

elif (A >= B):
    print("delicious")

elif (a+B >= X+1):
    print("dangerous")