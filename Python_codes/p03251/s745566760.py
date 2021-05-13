import sys
input = sys.stdin.readline


N,M,X,Y=list(map(int,input().split()))
x =list(map(int,input().split()))
y = list(map(int,input().split()))
x.append(X)
y.append(Y)

if min(y) - max(x) >0:
    print('No War')
else:
    print('War')

