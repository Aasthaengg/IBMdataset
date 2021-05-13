n=int(input())
p=list(map(int,input().split()))
m=0
d=[0]*n
t=set()
for i in range(n):
    if p[i]==i+1:
        d[i]=i+1
        m+=1
    if i!=0 and d[i]==1+d[i-1] and i-1 not in t:
        t.add(i)
print(m-len(t))