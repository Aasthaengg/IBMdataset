#G
N,M=map(int,input().split())
A=[[] for i in range(N+1)]
B=[0 for i in range(N+1)]
dp=[0 for j in range(N+1)]

for i in range(M):
    x,y=map(int,input().split())
    A[x].append(y)
    B[y]+=1

st=[]
for i in range(1,N+1):
    if B[i]==0:
        st.append(i)
        dp[i]

while len(st):
    x=st.pop()
    for y in A[x]:
        dp[y]=max(dp[y],dp[x]+1)
        B[y]-=1
        if B[y]==0:
            st.append(y)
print(max(dp))