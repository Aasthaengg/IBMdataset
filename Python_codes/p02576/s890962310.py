N,X,T = input().split()
M = 1 if int(N)%int(X) else 0
H = int(N)/int(X)
print((int(H) + M)*int(T))