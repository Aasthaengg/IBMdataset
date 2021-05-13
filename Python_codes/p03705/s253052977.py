n,a,b=map(int,input().split())
mn=(n-1)*a+b
mx=(n-1)*b+a
print(max(mx-mn+1,0))