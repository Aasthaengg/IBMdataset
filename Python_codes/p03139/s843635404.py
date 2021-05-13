n,a,b = map(int,input().split())
M=min(a,b)
m=a+b-n
if(m<0):
    m=0
print(M,m)
