n=int(input())
d,x=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
c=x
for i in range(n):
    h=0
    while(h*l[i]+1<=d):
        c=c+1
        h+=1
print(c)
