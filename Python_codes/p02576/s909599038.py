N,X,T = map(int,input().split())
if N % X == 0:
    a = N / X
    b = a * T
else:
    a = N // X + 1
    b = a * T
print(int(b))