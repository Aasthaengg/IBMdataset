N = int(input())
X = list(map(int,input().split()))
X_sorted = sorted(X)
midNL = X_sorted[N//2-1]
midNR = X_sorted[N//2]
for i in range(N):
    if X[i] <= midNL:
        print(midNR)
    else:
        print(midNL)