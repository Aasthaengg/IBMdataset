n,m,d = map(int, input().split())
print(((n-d)*2 if d else n)*(m-1)/n**2)