from collections import Counter
n = int(input())
X = list(map(int, input().split()))
c = Counter(X)
Xsort = sorted(X)

for i in range(n):
    if X[i]<Xsort[n//2]:
        print(Xsort[n//2])
    else:
        print(Xsort[n//2-1])
