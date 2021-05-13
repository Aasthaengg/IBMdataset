n,m = map(int,input().split())
ex = int((1900*m+100*(n-m))*(2**m))
print(ex)