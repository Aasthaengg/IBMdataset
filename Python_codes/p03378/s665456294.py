n,m,x=map(int,input().split())
l=list(map(int,input().split()))

low=sum(i>x for i in l)
hight=sum(i<x for i in l)

print(min(low,hight))