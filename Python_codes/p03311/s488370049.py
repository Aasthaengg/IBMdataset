
N = int(input())
A = list(map(int,input().split()))

X = []
for i in range(N):
    X.append(A[i]-(i+1))

X = sorted(X)
#bは数列Xの中央値
if N%2==1:
    b = X[N//2]
else:
    b = (X[N//2-1] + X[N//2]) / 2

out=0
for i in range(N):
    out+=abs(X[i] - b)

print(int(out))
