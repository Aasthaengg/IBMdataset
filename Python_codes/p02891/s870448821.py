import sys
S=input()
k=int(input())
ans=0
flag=0
left=0
right=0
if S[0]==S[-1]:
    left=1
    for i in range(len(S)-1):
        if S[i+1]==S[0]:
            left+=1
        else:
            break
    if left==len(S):
        print(left*k//2)
        sys.exit()
    right=1
    for i in range(len(S)-1):
        if S[-i-2]==S[0]:
            right+=1
        else:
            break
    
now=""
for i in range(left,len(S)-right):
    if flag==1:
        flag=0
        now=S[i]
        continue
    if now==S[i]:
        ans+=1
        flag=1
    now=S[i]
ans*=k

if S[0]==S[-1]:
    ans+=(left+right)//2*(k-1)
    ans+=left//2+right//2

print(ans)