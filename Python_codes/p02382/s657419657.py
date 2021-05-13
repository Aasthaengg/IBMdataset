n=int(input())
x=list(int(s) for s in input().split())
y=list(int(s) for s in input().split())
d=[(s-t,t-s)[s<t]for s,t in zip(x,y)]
f=lambda n:sum([s**n for s in d])**(1/n)
print(f(1),f(2),f(3),max(d),sep='\n')