n,d=map(int,input().split())
length=d*2+1
print(n//length if n%length==0 else n//length+1)