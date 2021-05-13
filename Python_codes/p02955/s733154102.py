from collections import deque
n,k=map(int,input().split())
a=list(map(int,input().split()))

asum=sum(a)


def divisor(n):
    divisors=[]
    for i in range(1,int(n**0.5+1)):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
div=divisor(asum)
#print(div)
b=[0]*n

ans=0
for d in div:
    count=0
    #print(d)
    #print(a)
    for i in range(n):
        b[i]=a[i]%d
    b.sort()
    #print(b)
    que=deque(b)
    #print(que)
    while que:
        s=que.popleft()
        if s==0:
            continue
        if len(que)==0:
            count=0
            break
        g=que.pop()
        #print(s,g)
        if s==d-g:
            count+=s
        if s<d-g:
            que.append(s+g)
            count+=s
        if s>d-g:
            que.appendleft(s-d+g)
            count+=(d-g)
    #print(d,count)
    if count<=k:
        ans=d
print(ans)
