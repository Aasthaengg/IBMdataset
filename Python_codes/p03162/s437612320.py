
# def solve(dp,L,i,j):
#     if i==len(dp):
#         return 0

#     else:
#         temp=0
#         for k in range(3):
#             if j!=k:
#                 temp=max(temp,L[i][k]+solve(dp,L,i+1,k))
#         dp[i]=temp
#         return dp[i]

T=int(input())
A=[]
for x in range(T):
    l=[int(i) for i in input().split()]
    A.append(l)
A.append([0,0,0])

for i in range(T-1,-1,-1):
    for j in range(3):
        temp=0
        for k in range(3):
            if j!=k:
                temp=max(temp,A[i][j]+A[i+1][k])

        A[i][j]=max(A[i][j],temp)
    # print(A)
    

print(max(A[0]))

