N=int(input())
ans=[]
for i in range(1,N):
    temp=(N-1)//i
    ans.append(temp)
Ans=sum(ans)
print(Ans)