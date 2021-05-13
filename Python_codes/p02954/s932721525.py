S=input()

goal=[]
ans=[0]*len(S)
for i in range(len(S)-1):
    if S[i:i+2]=='RL':
        goal.append(i)

for i in goal:
    cnt=0
    for l in range(i,-1,-1):
        if S[l]=='R':
            if cnt%2==0:
                ans[i]+=1
            else:
                ans[i+1]+=1
            cnt+=1
        else:
            break
    
    cnt=0
    for r in range(i+1,len(S)):
        if S[r]=='L':
            if cnt%2==0:
                ans[i+1]+=1
            else:
                ans[i]+=1
            cnt+=1
        else:
            break

print(*ans)