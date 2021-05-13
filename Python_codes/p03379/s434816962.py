n  = int(input())
X = list(map(int, input().split()))
X_sort = sorted(X)

mid1 = X_sort[n//2 - 1]
mid2 = X_sort[n//2]

for x in X:
    if x <= mid1:
        print(mid2)
    else:
        print(mid1)
