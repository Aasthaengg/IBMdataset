S=input()
K=int(input())
ans=0
last=S[0]
cnt=1
if len(set(S))>1:
    for i in range(1,len(S)):
        if S[i]==last:
            cnt+=1
        else:
            ans+=cnt//2
            cnt=1
            last=S[i]
    ans+=cnt//2
    ans*=K
    if S[0]==S[-1]:
        a,b=0,0
        last=S[0]
        for i in range(len(S)):
            if last==S[i]:
                a+=1
            else:
                break
        S=S[::-1]
        for i in range(len(S)):
            if last==S[i]:
                b+=1
            else:
                break
        ans-=(a//2+b//2-(a+b)//2)*(K-1)
else:
    ans=len(S)*K//2
print(ans)