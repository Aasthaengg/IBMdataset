N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)

sm=[]
count=0
for i in range(3*N):
    if count==N:
        break
    if i%2==1:
        sm.append(A[i])
        count+=1

ans=sum(sm)
print(ans)