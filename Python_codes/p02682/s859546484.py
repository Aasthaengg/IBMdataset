A, B, C, K = map(int, input().split())
if((K-A)>0):
    Y = K-A
else:
    print(K)
    exit()
if((Y-B)>0):
    Z = Y-B
else:
    Z = 0

X = A + 0 * Y + (-1) * Z
print(X)











	

