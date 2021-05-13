n,*i=map(int,open(0).read().split())
p=0
for l in range(n):
    a,b=i[-2-2*l:2*n-2*l]
    g=b-(a+p)%b if (a+p)%b!=0 else 0
    p+=g
print(p)