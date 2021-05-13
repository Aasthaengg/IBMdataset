n=int(input())
a=list(map(int,input().split()))
inf=float("inf")
M=max(a)
m=min(a)
data=[]
if abs(m)>abs(M):
    b=a.index(m)
    for i in range(n):
        data.append(str(b+1)+" "+str(i+1))
    for i in range(n-1):
        data.append(str(n-i)+" "+str(n-i-1))
else:
    b=a.index(M)
    for i in range(n):
        data.append(str(b+1)+" "+str(i+1))
    for i in range(1,n):
        data.append(str(i)+" "+str(i+1))
print(len(data))
for u in data:
    print(u)