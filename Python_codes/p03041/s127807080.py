a,b=map(int,input().split())
c=input()
n=c[b-1]
n=n.lower()
c=list(c)
c[b-1]=n
c=''.join(c)
print(c)