n,t=map(int,input().split())
x=[int(x) for x in input().split()]
lost=0
for i in range(1,n):
    if x[i]-x[i-1]<t:
        lost+=t-(x[i]-x[i-1])
        
print(t*n-lost)