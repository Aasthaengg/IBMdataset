n=int(input())
list_1=list(map(int,input().split()))
list_2=list(map(int,input().split()))
ans=0
for i in range(n):
    sum_=sum(list_1[:i+1])+sum(list_2[i:])
    ans=max(ans,sum_)
print(ans)