#C - Traveling Plan
N = int(input())
A = list(map(int, input().split()))
DP = []
ans = []
DP.append(abs(0-A[0]))
for i in range(1,N):
    DP.append(abs(A[i]-A[i-1]))

sum_DP = sum(DP)

for j in range(N):
    if j == 0:
        tmp = sum_DP-DP[0]-DP[1]+abs(A[1])+abs(A[N - 1])
    elif j == N-1:
        tmp = sum_DP-DP[N-1]+abs(A[N - 2])
    else:
        tmp = sum_DP + abs(A[N - 1])-DP[j]-DP[j+1]+abs(A[j+1]-A[j-1])
    ans.append(tmp)

for i in range(len(ans)):
    print(ans[i])