X, N = map(int,input().split())
P = list(map(int,input().split()))
list = [0] * 102
res = X
dist = 102
for p in P:
    list[p] = 1
for i in range(102):
    if list[i] == 0:
        if abs(i - X) < dist:
            dist = abs(i - X)
            res = i
        elif abs(i - X) == dist:
            res = min(res,i)
print(res)
