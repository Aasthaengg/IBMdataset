n=int(input())
s=input()
ans=s.count('.')
cnt=ans

for i in s:
    if i=='.':
        cnt-=1
        ans=min(ans,cnt)
    
    else:
        cnt+=1

ans=min(ans,cnt)


print(ans)