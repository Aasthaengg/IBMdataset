N,S=int(input()),input()
ans=0
for i in range(1,N):
    a,b,c=S[:i],S[i:],0
    for j in range(97,123):
        if chr(j)in a and chr(j)in b:c+=1
    ans=max(ans,c)
print(ans)