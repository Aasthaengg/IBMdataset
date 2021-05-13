X = int(input())

while(True):
    for i in range(2, X):
        if(X % i == 0):
            break
    else:
        print(X)
        break
    X += 1
