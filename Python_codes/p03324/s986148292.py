d,n=map(int,input().split())
x=n*(100**d)
print(x if n%100!=0 else x+(100**d))