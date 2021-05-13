import copy
N = int(input())
X = [int(i) for i in input().split()]
Y = copy.deepcopy(X)
Y = sorted(Y, key= lambda x: -x)

c = int(N/2)

for i in range(N):
    a = X[i]
    if a >= Y[c-1]:
        print(Y[c])
    else:
        print(Y[c-1])