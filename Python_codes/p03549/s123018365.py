n,m = map(int,input().split())
x = 1900*m + 100*(n-m)
p = 1/2**m
print(int(x//p))
