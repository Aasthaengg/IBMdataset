N=int(input())
S=[]
ans=0
for i in range(N):
    s=int(input())
    S.append([s,s%10])
    ans+=s

if ans%10!=0:
    print(ans)
    exit()

S.sort(key=lambda x:x[0])
for i in range(N):
    if S[i][1]!=0:
        ans-=S[i][0]
        print(ans)
        exit()
print(0)