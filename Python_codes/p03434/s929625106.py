n,*x=map(int,open(0).read().split());a=0;t=1;x.sort()
while x:a+=t*x.pop();t*=-1
print(a)