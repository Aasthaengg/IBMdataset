S=list(input())
nowb=0
ans=0
for i in range(len(S)):
    s=S[i]
    if s=="B":
        nowb+=1
    else:
        ans+=nowb
        S[i]="B"

print(ans)
#print(S)