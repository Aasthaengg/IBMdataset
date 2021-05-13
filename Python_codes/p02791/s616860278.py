n,*p=map(int,open(0).read().split())
c=0
min_p=p[0]
for i in range(n):
    min_p=min(min_p,p[i])
    if p[i]<=min_p:
        c+=1
print(c)