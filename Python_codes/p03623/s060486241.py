x,a,b=map(int,input().split())
c=abs(x-a)
d=abs(x-b)
print('A' if c<d else 'B')