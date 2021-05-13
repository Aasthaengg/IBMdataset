n,c,k=map(int,input().split())
ans=0
cnt=1
t=sorted([int(input())for s in range(n)])
while t:
    now=t.pop()
    ans+=1
    while t and cnt<c and t[-1]+k>=now:
        cnt+=1
        t.pop()
    cnt=1

print(ans)