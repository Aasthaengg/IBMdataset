N=int(input())
A=list(map(int,input().split()))
A.sort()
flag=[0]*N
ans=[]
for i in range(1,N-1):
    if A[i]<0:
        ans.append([A[-1],A[i]])
        A[-1]-=A[i]
    else:
        ans.append([A[0],A[i]])
        A[0]-=A[i]
ans.append([A[-1],A[0]])
M=A[-1]-A[0]
print(M)
for u in ans:
    print(*u)