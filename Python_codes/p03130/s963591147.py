ab=[list(map(int,input().split(" "))) for _ in range(3)]
d=[]
for i in ab:
    d.append(i[0])
    d.append(i[1])
if d.count(1)>=3 or d.count(2)>=3 or d.count(3)>=3 or d.count(4)>=3:
    print("NO")
else:
    print("YES")