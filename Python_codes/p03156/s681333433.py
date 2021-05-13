n=int(input())
a,b=map(int,input().split())
p=[int(i) for i in input().split()]
x=sum(i<=a for i in p)
y=sum(a<i<=b for i in p)
z=sum(b<i for i in p)
print(min(x,y,z))