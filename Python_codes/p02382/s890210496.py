n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
d=[abs(s-t)for s,t in zip(x,y)]
f=lambda n:sum([s**n for s in d])**(1/n)
print(f(1),f(2),f(3),max(d),sep='\n')
