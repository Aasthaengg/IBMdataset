S=input()
l=len(S)
dp1=[0]*l
dp2=[0]*l
dp1[0]=1
for i in range(1,l):
    if S[i-1]!=S[i]:
        dp1[i]=max(dp1[i-1],dp2[i-1])+1
    else:
        dp1[i]=dp2[i-1]+1
    if i==1:
        dp2[i]=1
        continue
    if i==2:
        dp2[i]=max(dp1[i-2],dp2[i-2])+1
        continue
    if S[i-3:i-1]!=S[i-1:i+1]:
        dp2[i]=max(dp1[i-2],dp2[i-2])+1
    else:
        dp2[i]=dp1[i-2]+1
    
print(max(dp1[l-1],dp2[l-1]))