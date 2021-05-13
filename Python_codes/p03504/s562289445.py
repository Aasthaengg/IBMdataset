n,C=map(int,input().split())
schedule=[]
time=[[0 for i in range(C)] for j in range(2*10**5+2)]

for i in range(n):
    s,t,c=map(int,input().split())
    schedule.append([s,t,c])

schedule.sort()

for s,t,c in schedule:
    if time[2*s][c-1]==-1:
        time[2*s][c-1]+=1
    else:
        time[2*s-1][c-1]+=1
    time[2*t][c-1]-=1

for i in range(2*10**5+1):
    for j in range(C):
        time[i+1][j]+=time[i][j]
ans=1
for i in range(2*10**5+2):
    tmp=0
    for j in range(C):
        tmp+=time[i][j]
    ans=max(ans,tmp)

print(ans)


