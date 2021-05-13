N,X,T = map(int, input().split())

if N % X == 0:
    result = int(N / X * T) 
else:
    result = int((N // X + 1) * T)
print(result)