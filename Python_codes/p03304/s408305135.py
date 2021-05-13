n,m,d=map(int,input().split())
def prob(n,d):
    return (1 if d==0 else 2)*(n-d)/(n**2)
print((m-1)*prob(n,d))