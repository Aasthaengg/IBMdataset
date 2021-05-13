n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a+b,a,b))
l.sort(reverse=True)
k=0
x=0
y=0
while k<n:
    if k%2==0:
        x+=l[k][1]
    else:
        y+=l[k][2]
    k+=1
print(x-y)