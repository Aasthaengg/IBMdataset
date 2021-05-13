X = list(map(int, input().split()))
i = 0
while i < len(X):
    if X[i] == 0:
        print(i+1)
    i +=1