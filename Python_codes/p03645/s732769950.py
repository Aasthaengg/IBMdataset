n,m=map(int,input().split())
lst=[]
for i in range(m):
    lst.append(list(map(int,input().split())))

front=[]
back=[]

for i in lst:
    if i[0]==1:
        front.append(i[1])

for i in lst:
    if i[1]==n:
        back.append(i[0])
front=set(front)
back=set(back)
print("POSSIBLE" if len(front&back)>=1 else "IMPOSSIBLE")