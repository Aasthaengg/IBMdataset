n = int(input())
X = list(map(int, input().split()))

Y = X[::]
Y.sort()

m = n // 2
median = (Y[m] + Y[m - 1]) / 2

for x in X:
    if x < median:
        print(Y[m])
    else:
        print(Y[m-1])

