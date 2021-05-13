n, m, d = map(int, input().split())
tmp = (n-d)*2 if d>0 else n
print(tmp*(m-1)/n/n)