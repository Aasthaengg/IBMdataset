import copy

n = int(input())

X = list(map(int,input().split()))

XX = copy.deepcopy(X)
XX.sort()
high = XX[n//2]
low = XX[n//2-1]

for i in range(n):
    if high == low:
        print(high)
        continue
    if X[i] < high:
        print(high)
    else:
        print(low)