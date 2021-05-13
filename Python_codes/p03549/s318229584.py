n,m = map(int,input().split())
r = 1-1/(2**m)
print(int((1900*m+100*(n-m))/(2**m)/(1-r)**2))
