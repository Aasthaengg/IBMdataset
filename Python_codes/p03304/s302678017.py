n,m,d=map(int,input().split())
if d==0:
    bai= n 
else:
    bai= 2*(n-d)
print( (m-1)*bai/n/n )