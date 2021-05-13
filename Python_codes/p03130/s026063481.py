route=[0]*4
for _ in range(3):
    a,b=map(int,input().split())
    route[a-1]+=1
    route[b-1]+=1

if route[0]==route[3]==1 and route[1]==route[2]==2:
    print("YES")
else:
    print("NO")
