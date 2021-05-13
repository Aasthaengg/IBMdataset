n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a+b,a,b))
l.sort(reverse=True)
t,a=0,0
for i in range(0,n,2):
    t+=l[i][1]
for i in range(1,n,2):
    a+=l[i][2]
print(t-a)