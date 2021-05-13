n=int(input())
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
sm=sum(a)
ans=1
pas=a[0]
for i in range(1,n):
    if a[i-1]>(sm-pas)*2:
        break
    ans += 1
    pas += a[i]
print(ans)
