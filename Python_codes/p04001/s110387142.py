import copy
a=list(input())
ano=list(range(1,100,2))
n=len(a)-1
ans=0
for i in range(2**n):
    c=copy.deepcopy(a)
    b=['']*n
    for j in range(n):
        if ((i>>j)&1)==1:
            b[j]='+'
    for k in range(n):
        c.insert(ano[k],b[k])
    ans+=eval(''.join(c))
print(ans)

