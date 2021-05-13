n=int(input())
plan=[[int(s) for s in input().split()] for j in range(n)]
now =[0 for j in range(3)]
plan.insert(0,now)
ans=0
for i in range(n):
    dt=abs(plan[i+1][0]-plan[i][0])
    dx=abs(plan[i+1][1]-plan[i][1])
    dy=abs(plan[i+1][2]-plan[i][2])
    if dt>=dx+dy:
        if dt%2 == (dx+dy)%2:
            ans+=1
print("Yes" if ans==n else "No")