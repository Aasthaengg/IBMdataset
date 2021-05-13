import sys,bisect

input=sys.stdin.readline

N=int(input())
robot=[]
for i in range(N):
    X,L=map(int,input().split())
    robot.append((X+L,L))

robot.sort()
pos=[robot[i][0] for i in range(N)]
arm=[-1]*N
for i in range(0,N):
    index=bisect.bisect_right(pos,robot[i][0]-2*robot[i][1])
    arm[i]=index-1

dp=[0]*N
dp[0]=1
Max=[0]*N
Max[0]=1
for i in range(1,N):
    if arm[i]==-1:
        dp[i]=1
    else:
        dp[i]=1+Max[arm[i]]
    Max[i]=max(dp[i],Max[i-1])

print(max(dp))