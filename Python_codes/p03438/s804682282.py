N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
x, y = sum(X), sum(Y)
import sys
if y < x:
    print("No")
    sys.exit()
kx=ky=y-x
for i in range(N):
    if Y[i] > X[i]:
        kx -= -(-(Y[i]-X[i])//2)
        X[i] = Y[i] + (Y[i]-X[i])%2
for i in range(N):
    if X[i] > Y[i]:
        ky -= X[i]-Y[i]
        Y[i] = X[i]
#print(X, Y, kx, ky, y-x)
if kx <0 or ky<0:
    print("No")
elif kx*2 != ky:
    print("No")
else:
    print("Yes")
