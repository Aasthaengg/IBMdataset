n=int(input())
s=str(input())
ans=0

for i in range(n-1):
    n=i+1
    if s[n]=='E':
        ans=ans+1

cnt=ans

for i in range(n):
    if s[i:i+2]=='WW':
        cnt=cnt+1
    elif s[i:i+2]=='EE':
        cnt=cnt-1
    else:
        0
        
    #print('i,s[i:i+2],ans,cnt',i,s[i:i+2],ans,cnt)
    ans=min(ans,cnt)
print(ans)
