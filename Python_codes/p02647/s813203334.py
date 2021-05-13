from numba import njit

@njit(cache=True)
def aaa(n,k,a):
    for f in range(k):
        a1=[0]*(n+1)
        for x in range(n):
            y=max(0,x-a[x])
            a1[y]=a1[y]+1    
            z=min(n-1,x+a[x])
            a1[z+1]=a1[z+1]-1
        a[0]=a1[0]
        for x in range(1,n):    
            a[x]=a[x-1]+a1[x]
        if a==[n]*n:
            break
    return a

x=input()
x0=x.split()
n=int(x0[0])
k=int(x0[1])
a0=input()
a0=a0.split()
a=[int(s) for s in a0]

b=aaa(n,k,a)
for i in range(n):
    print(b[i])