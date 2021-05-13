from collections import Counter

n,t = map(int,input().split())
a = list(map(int,input().split()))
a_min = [0] * n
a_min[0] = a[0]
for i in range(1,n):
    a_min[i] = min(a_min[i-1],a[i])

profit = [a[i] - a_min[i] for i in range(n)]

comb = Counter(profit)
print(sorted(comb.items(),reverse = True)[0][1])