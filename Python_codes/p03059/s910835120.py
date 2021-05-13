a,b,t=map(int,input().split())
n=1
while t>=n*a:
    n+=1
print((n-1)*b)