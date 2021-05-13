N=int(input())
s=[int(input())for i in range(N)]
s.sort()
ans=0
if(sum(s))%10:
        ans=max(ans,sum(s))
else:
    for i in s:
        if(sum(s)-i)%10:
            ans=max(ans,sum(s)-i)
print(ans)