n,m = map(int,input().split())
p = 2**m
r = (p-1)/p
print(int((1900*m + 100*(n-m))//(1-r)))