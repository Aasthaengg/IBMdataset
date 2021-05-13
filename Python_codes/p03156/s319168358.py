n=int(input())
a,b=map(int,input().split())
p=sorted(list(map(int,input().split())))

l1=[]
l2=[]
l3=[]

for i in range(n):
    if p[i]<=a:
        l1.append(p[i])

for i in range(n):
    if a+1<=p[i]<=b:
        l2.append(p[i])
        
for i in range(n):
    if b<p[i]:
        l3.append(p[i])
        
print(min(len(l1),len(l2),len(l3)))