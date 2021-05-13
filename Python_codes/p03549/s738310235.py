n,m = map(int,input().split())
a = 1900*m+100*(n-m)
print(a+a*(2**m-1))