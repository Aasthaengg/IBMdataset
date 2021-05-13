n,x=map(int,input().split())
m=[]
for i in range(n):
    m.append(int(input()))
#print(m)
for i in range(n):
    x-=m[i]
#print(x)
count=x//min(m)
print(len(m)+count)