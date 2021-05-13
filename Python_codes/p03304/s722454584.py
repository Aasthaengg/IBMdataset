n,m,d=list(map(int,input().split()))

def sum(a,b):
    return (a+b)*(a+b+1)/2

def calc_between(n):
    if d==0:
        return n
    ans=n
    if 2*d+1<=n:
        ans+=(n-2*d)
    return ans

x=calc_between(n)
print((m-1)*x/n**2)