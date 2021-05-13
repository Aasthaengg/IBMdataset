n=int(input())
lst=list(map(int,input().split()))
m1=0
for i in range(n):
    if i%2==0:
        m1+=lst[i]
    else:
        m1-=lst[i]
ans=[m1]
for i in range(n-1):
    tmp=lst[i]
    tmp-=ans[-1]//2
    ans.append(tmp*2)
print(*ans)