n = int(input())
X = list(int(x) for x in input().split())
Y = sorted(X)
mid1 = Y[(n//2)-1]
mid2 = Y[n//2]
for x in X:
    if x <= mid1:
        print(mid2)
    else:
        print(mid1)