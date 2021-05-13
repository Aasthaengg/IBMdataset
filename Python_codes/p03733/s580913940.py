n,s=map(int,input().split())
t=list(map(int,input().split()))
ans=0
stop=0
for i in range(n):
    if stop>t[i]:
        ans+=max(0,s-(stop-t[i]))
    else:
        ans+=s
    stop=t[i]+s
print(ans)