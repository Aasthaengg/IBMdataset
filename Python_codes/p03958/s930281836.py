K,T=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A,reverse=True) #大きい順
ans=A[0]-1 #被る日
for i in range(1,T): 
    ans-=A[i]
    if ans<0:
        ans=0
        break
print(ans)