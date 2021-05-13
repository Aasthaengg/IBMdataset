from math import ceil
n = int(input())
data = list(map(int, input().split()))
n = max(data)
nn = n/2.0
r = min((d for d in data if d != n), key=lambda x: abs(nn-x))
print(n, r)