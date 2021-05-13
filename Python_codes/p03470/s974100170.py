n=int(input())
d=[]
for i in range(n):
    d.append(int(input()))
ans=1
d=sorted(d)
for i in range(n-1):
    if d[i]!=d[i+1]:
        ans+=1
print(ans)

