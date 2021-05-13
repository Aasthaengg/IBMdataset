town=[0 for _ in range(4)]
for i in range(3):
    a,b=map(int,input().split())
    town[a-1]+=1
    town[b-1]+=1
if town.count(1)==2 and town.count(2)==2:
    print('YES')
else:
    print('NO')