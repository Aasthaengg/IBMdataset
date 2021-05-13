
while True:
    n=int(input())
    if n==0:
        break
    lst=list(map(float, input().split()))
    s=sum(lst)  
    a=s/n
    ans=0
    for i in range(n):
        ans+=((lst[i]- a)**2)/n
    ans=ans**0.5
    print(ans)
