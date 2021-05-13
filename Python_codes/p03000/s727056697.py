n,x=map(int,input().split())
l=list(map(int,input().split()))
s=[0]
d=0
y=0
for i in range(n):
    d=d+l[i]
    s.append(d)
for i in range(n+1):
    if s[i]<=x:
        y+=1
print(y)