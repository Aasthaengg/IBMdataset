X = int(input())
H = X // 3600
X = X%3600
M = X // 60
X %= 60
print(str(H)+":"+str(M)+":"+str(X))

