N, K = map(int,input().split())
A = list(map(int, input().split()))
S = [0]*(N+1)
S2 = [0]*(N+1)
dict = {}#最新K件の度数分布の管理

for i in range(N):
    S[i+1]=S[i]+A[i]
    S2[i+1] =(S[i+1]-i-1)%K

ans =0
for i in range(N+1):
    if dict.get(S2[i],0):
        ans += dict[S2[i]]
    dict[S2[i]]=dict.get(S2[i],0)+1
    if i >=K-1:
        dict[S2[i-(K-1)]]-=1

print(ans)