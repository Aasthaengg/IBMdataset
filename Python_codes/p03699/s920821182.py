n=int(input())
s=[int(input()) for i in range(n)]
s.sort()
ans=sum(s)
if sum(s)%10==0:
    for i in range(n):
        if s[i]%10!=0:
            ans-=s[i]
            break
    else:
        ans=0
print(ans)