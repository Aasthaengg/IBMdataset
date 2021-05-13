N = int(input())
S = list(input())

W_count = [0]*(N)#左から累積を数えていく
E_count = [0]*(N)#右からｒｙ

for i in range(1,N,1):
    W_count[i]=W_count[i-1]
    if S[i-1]=="W":
        W_count[i]+=1

for i in range(N-2,-1,-1):
    E_count[i]=E_count[i+1]
    if S[i+1]=="E":
        E_count[i]+=1

ans = [0]*(N)
for i in range(0,N,1):
    ans[i]=W_count[i]+E_count[i]

print(min(ans))