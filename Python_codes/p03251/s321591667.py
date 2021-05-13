n,m,x,y=map(int,input().split())
xx=[int(i) for i in input().split()]
yy=[int(i) for i in input().split()]
ok=False
for i in range(x+1,y+1):
    ansx=[0 if j<i else 1 for j in xx]
    ansy=[0 if j>=i else 1 for j in yy]
    if 1 not in ansx and 1 not in ansy:
        ok=True
        break
if ok:
    print("No War")
else:
    print("War")