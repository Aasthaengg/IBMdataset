a=input()
r=[]
for i in range(a):
    k=input()
    r.append(k)
minv=r[0]
maxv=-10**9
for j in range(1,len(r)):
    maxv=max(maxv,r[j]-minv)
    minv=min(minv,r[j])
print maxv