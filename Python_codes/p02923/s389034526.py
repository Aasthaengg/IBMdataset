N,*H=map(int, open(0).read().split())
tmp=0
ans=0
for n in range(N-1):
    if H[n]>=H[n+1]:
        tmp+=1
    else:
        ans=max(tmp,ans)
        tmp=0
print(max(tmp,ans))