nab=list(map(int,input().split()))
v=list(map(int,input().split()))
v.sort(reverse=True)
vmin=v[:nab[1]]
print(sum(vmin)/len(vmin))
mini=1
if nab[1]>1:
    for i in range(nab[1]-1):
        if vmin[-2-i]==vmin[-1]:
            mini+=1
        else:
            break
ex=0
for i in range(nab[0]-nab[1]):
    if v[nab[1]+i]==vmin[-1]:
        ex+=1
    else:
        break
def f(n):
    out=1
    for i in range(1,n+1):
        out*=i
    return out
ans=0
if vmin[0]!=vmin[-1]:
    ans=f(mini+ex)//(f(mini)*f(ex))
    print(ans)
else:
    m=min(nab[2]-nab[1],ex)
    for i in range(m+1):
        ans+=f(mini+ex)//(f(mini+i)*f(ex-i))
    print(ans)
