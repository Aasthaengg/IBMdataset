from collections import Counter

def comb(x,y):
    c=1
    for i in range(y):
        c*=(x-i)
        c//=(i+1)
    return c

n,a,b=map(int,input().split())
V=list(map(int,input().split()))
V.sort(reverse=True)
print(sum(V[:a])/a)
c=Counter(V)
cnt=0
for v in V:
    i=c[v]
    cnt+=i
    if cnt>=a:
        break
if V[0]==V[a-1]:
    ans=0
    for j in range(a,min(cnt,b)+1):
        ans+=comb(i,j)
    print(ans)
else:
    print(comb(i,a+i-cnt))