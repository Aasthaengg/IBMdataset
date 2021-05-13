S=input()
N=len(S)
As=[0]*N
ABs=[0]*N
ABCs=[0]*N
p=10**9+7

if S[0]=="A":
    As[0]=1

now=1
if S[0]=="?":
    now=3
    As[0]=1
for i in range(1,N):
    s=S[i]
    if s=="A":
        As[i]=(As[i-1]+now)%p
        ABs[i]=ABs[i-1]
        ABCs[i]=ABCs[i-1]
    elif s=="B":
        As[i]=As[i-1]
        ABs[i]=(ABs[i-1]+As[i-1])%p
        ABCs[i]=ABCs[i-1]

    elif s=="C":
        As[i]=As[i-1]
        ABs[i]=ABs[i-1]
        ABCs[i]=(ABCs[i-1]+ABs[i-1])%p

    else:
        
        As[i]=(3*As[i-1]+now)%p
        ABs[i]=(3*ABs[i-1]+As[i-1])%p
        ABCs[i]=(3*ABCs[i-1]+ABs[i-1])%p
        now*=3
        now%=p

print(ABCs[-1])
#print(As)
#print(ABs)
#print(ABCs)