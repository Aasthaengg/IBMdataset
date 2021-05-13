N=int(input())
v=list(map(int,input().split()))
v.sort()
v.reverse()

for i in range(N):
    v[i]=v[i]/(2**(i+1))
    if i==N-1:
        v[i]=v[i]*2

ans=sum(v)

print(ans)