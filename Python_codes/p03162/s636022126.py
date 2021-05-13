N = int(input())
ABC = []
for _ in range(N):
    line = list(map(int,input().split()))
    ABC.append(line)
DP = [ABC[0]]
for i in range(1,N):
    a = ABC[i][0] + max(DP[i-1][1],DP[i-1][2])
    b = ABC[i][1] + max(DP[i-1][2],DP[i-1][0])
    c = ABC[i][2] + max(DP[i-1][0],DP[i-1][1])
    DP.append([a,b,c])
print(max(DP[-1]))