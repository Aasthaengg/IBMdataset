n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a+b,a,b))
l.sort(reverse=True)
c1=0
c2=0
for i in range(n):
    if i%2==0:
        c1+=l[i][1]
    else:
        c2+=l[i][2]
print(c1-c2)