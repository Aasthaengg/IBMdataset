a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
d.append(a-c[b-1]+c[0])
for i in range(b-1):
    d.append(c[i+1]-c[i])
print(sum(d)-max(d))