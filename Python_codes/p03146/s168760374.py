s=int(input())
S=[]
ans=0
for i in range(10**6):
    S.append(s)
    if s%2==0 :
        s=s//2
    else:
        s=3*s+1
    for j in range(i):
        if S[j]==s:
            ans=i+1
            break
    if ans!=0 :
        break            
print(ans+1)