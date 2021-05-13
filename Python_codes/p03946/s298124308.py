n, t = map(int, input().split())
a = list(map(int, input().split()))
profit = [0]
minm = 10 ** 9
for i in range(n):
    minm = min(minm, a[i])
    profit.append(a[i] - minm)
print(profit.count(max(profit)))