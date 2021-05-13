import sys
X = int(input())
a = 0
if X <= 2:
    print(X)
else:
    for i in range(1,X):
        a += i
        if a >= X:
            print(i)
            sys.exit()