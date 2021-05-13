_,*a=map(int,open(0).read().split())
l=[*map(abs,a)]
print(sum(l)-sum(i<0 for i in a)%2*min(l)*2)