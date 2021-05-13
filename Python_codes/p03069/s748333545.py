n=int(input());a=[0];b=[0];s=0
for i in input():t=i=='.';b+=[b[-1]+1-t*2];s+=t
print(min([i+s for i in b]))