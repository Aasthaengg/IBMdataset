import sys
X = int(input())
while True:
    OK = True
    for i in range(2, X):
        if X % i == 0:
            X += 1
            OK = False
            break
    if OK:
        print(X)
        break