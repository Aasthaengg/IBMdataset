N,M=map(int,input().split())
n=[0,1,2,3,4,5,6,7,8,9]
H=[0,2,5,5,4,5,6,3,7,6]

L=[]
A=list(map(int,input().split()))
A.sort(reverse=True)

for i in range(M):
    for j in range(10):
        if A[i]==n[j]:
            L.append([H[j],n[j]])
#print(L)
dp=["" for i in range(N+1)]
dp[0]="0"
for i in range(len(L)):
    for j in range(L[i][0],N+1):
        if dp[j-L[i][0]]!="":
            if len(dp[j])>len(dp[j-L[i][0]]+str(L[i][1])):
                continue
            elif len(dp[j])<len(dp[j-L[i][0]]+str(L[i][1])):
                dp[j]=dp[j-L[i][0]]+str(L[i][1])
            else:
                if dp[j]<dp[j-L[i][0]]+str(L[i][1]):
                    dp[j]=dp[j-L[i][0]]+str(L[i][1])
print(dp[N][1:])