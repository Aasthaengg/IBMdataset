n,*a=map(int,open(0).read().split())
b=list(map(abs,a))
print(sum(b)-sum(i<0 for i in a)%2*min(b)*2)