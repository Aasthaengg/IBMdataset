from itertools import*;r=p=0
for k,g in groupby(input()):x=len(list(g));r=r+x*(x+1)//2-min(x,p)*(k=='>');p=x
print(r)