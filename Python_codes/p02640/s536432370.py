import sys

X, Y = map(int,input().split()) #X_動物の数　Y_脚の数


ALL = X*2
for i in range(X+1):
    if ALL == Y:
        print('Yes')
        sys.exit()
    
    ALL += 2

print('No')