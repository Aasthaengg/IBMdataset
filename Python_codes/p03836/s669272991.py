sx,sy,tx,ty=map(int,input().split())

countx=tx-sx
county=ty-sy

ans=[]
for i in range(county):
    ans.append("U")
for i in range(countx):
    ans.append("R")

for i in range(county):
    ans.append("D")
for i in range(countx):
    ans.append("L")

ans.append("L")

for i in range(county+1):
    ans.append("U")
for i in range(countx+1):
    ans.append("R")
ans.append("D")

ans.append("R")

for i in range(county+1):
    ans.append("D")
for i in range(countx+1):
    ans.append("L")

ans.append("U")

Z=[str(a) for a in ans]
Z="".join(Z)
print(Z)
