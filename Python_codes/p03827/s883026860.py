N=int(input())
S=input()
SS=S.replace("I","1,").replace("D","-1,").split(",")
cnt=0
ans=0
for i in range(N):
    cnt+=int(SS[i])
    ans=max(ans,cnt)
print(ans)