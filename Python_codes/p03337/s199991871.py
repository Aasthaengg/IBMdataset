n, m = map(int, input().split())
k = sorted([n+m, n-m, n*m], reverse=True)
print(k[0])