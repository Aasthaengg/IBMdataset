n, m=map(int, input().split())
p=[0]+list(map(int, input().split()))

par=[i for i in range(n+1)]
cnt=0
def root(i):
    if par[i]==i:
        return i
    else:
        par[i]=root(par[i])
        return par[i]


for i in range(m):
    x, y=map(int, input().split())
    if root(x)==root(y):
        0
        #print(par[1:])
    else:
        par[root(y)]=root(x)
        #print(par[1:])

ans=0
for i in range(n):
    n=1+i
    if root(n)==root(p[n]):
        ans=ans+1
print(ans)
'''
print(par[1:])

root_ls=[0]+[root(i+1) for i in range(n)]
print(par[1:])
print(root_ls[1:])
'''
