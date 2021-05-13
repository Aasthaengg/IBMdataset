n,*a=map(int,open(0).read().split())
b=sum(i<0 for i in a)%2
a=list(map(abs,a))
print(sum(a)-min(a)*2*b)