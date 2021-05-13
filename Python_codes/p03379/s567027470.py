n = int(input())
X = tuple(map(int, input().split()))
Xs = sorted(X)

ml = Xs[n//2-1]
mr = Xs[n//2]

for i in range(n):
    if X[i] <= ml:
        print(mr)
    else:
        print(ml)
