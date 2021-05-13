n,*a=map(int,open(0).read().split())
b=sum([i<0 for i in a])%2
a=[abs(i) for i in a]
print(sum(a) if b==0 or 0 in a else sum(a)-min(a)*2)