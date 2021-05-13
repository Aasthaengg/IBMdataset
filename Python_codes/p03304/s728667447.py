n,m,d=map(int,input().split())

if d==0:
    a=(1/n)*(m-1)
elif n>=d*2+1:
    a=((n-d*2)/n*(2/n)+2*d/n*(1/n))*(m-1)
else :
    a=(d/n)*(m-1)
#n%d==0
print(a)
