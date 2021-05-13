N=int(input())
A=list(map(int,input().split()))
ans=0
for num in A:
    count=0
    while num%2==0:
        num=num//2
        count+=1
    ans+=count

print(ans)