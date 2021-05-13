n=int(input())
l=[]
x=0
for i in range(n):
    l.append(int(input()))
y=l.index(max(l))

for i in range(n):
    if i==y:
        x+=l[i]//2
    else:
        x+=l[i]
             
print(x)