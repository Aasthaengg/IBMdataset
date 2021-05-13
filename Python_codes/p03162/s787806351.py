n = int(input())
prev_dp=[0]*3
for _ in range(n):
    arr=[]
    a,b,c = list(map(int,input().split()))
    arr.append((a,b,c))
    curr_dp = [0]*3
    for i in range(3):
        for j in range(3):
            if i!=j:
                #print(i,j)
                curr_dp[j] = max(curr_dp[j],prev_dp[i] + arr[0][j])
    prev_dp = curr_dp
print(max(prev_dp[0],prev_dp[1],prev_dp[2]))