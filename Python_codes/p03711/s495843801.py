d={s:1 for s in [4,6,9,11]}
for i in [1,3,5,7,8,10,12]:
    d[i]=0
d[2]=2
a,s=map(int,input().split())
print("Yes")if d[a]==d[s] else print("No")