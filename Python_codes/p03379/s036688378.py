N = int(input())
X = [int(i) for i in input().split()]
sX = sorted(X)

mid = N // 2 - 1
l = sX[mid]
r = sX[mid+1]
for i in range(N):
    if X[i] <= l:
        print(r)
    else:
        print(l)