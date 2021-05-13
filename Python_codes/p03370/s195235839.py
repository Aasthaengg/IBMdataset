n,x=map(int,input().split())
donut=[]
ans=0
sum_num=0
for i in range(n):
    m=int(input())
    ans+=1
    donut.append(m)
sum_num+=sum(donut)
min_num=min(donut)
while(1):
    if sum_num>x:
        break
    ans+=1
    sum_num+=min_num
print(ans-1)