n,c,*a=map(int,open(0).read().split())
for i in a:c^=i
print('YNeos'[c>0::2])