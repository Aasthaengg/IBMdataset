n,m=map(int,input().split())
a=[]
b=[]
for i in range(m):
    ab=list(map(int,input().split()))
    a.append(ab[0])
    b.append(ab[1])

islands1=set() #islands can reach from island 1
islands2=set() #islands can reach to island N

for i in range(m):
    if a[i]==1:
        islands1.add(b[i])
    
    if b[i]==n:
        islands2.add(a[i])

ans=islands1 & islands2
print("POSSIBLE" if ans else "IMPOSSIBLE")