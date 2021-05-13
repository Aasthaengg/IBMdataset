N=int(input());r=[0]
def s(n,p=1,a=1,k=0):
 if n<0:p,a,k=-2,-2,1
 while abs(n)>abs(a):p*=4;a+=p;k+=2
 r[0]|=1<<k
 if n-p:s(n-p)
if N:s(N)
print(bin(r[0])[2:])
