N,M=map(int,input().split())
AB=[]
for i in range(N):
    AB.append(list(map(int,input().split())))
AB.sort(key=lambda x: x[0])

max_=0
for i in AB:
    if max_<i[0]:
        max_=i[0]

dp=[0]*(max_+M)
max_=0
for i in AB:
    for j in range(M)[::-1]:
        dp[j+i[0]] = max(dp[j+i[0]],dp[j]+i[1])
        
print(max(dp))