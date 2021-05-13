n, m, d = map(int, input().split())
print((m-1) * ((n-d)*2 if d!=0 else n) / (n*n))
