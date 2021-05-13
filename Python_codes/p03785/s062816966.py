N,C,K=map(int,input().split())
arrive=[]
c=0
for i in range(N):
    temp=int(input())
    arrive.append(temp)

arrive.sort()
sw=False
ans=0

for j in range(N):
    if sw==False:
        lim=arrive[j]+K
        c+=1
        sw=True
    else:
        c+=1
    if j<N-1:
        if c==C or lim<arrive[j+1]:
            ans+=1
            c=0
            sw=False
    else:
        ans+=1
print(ans)
