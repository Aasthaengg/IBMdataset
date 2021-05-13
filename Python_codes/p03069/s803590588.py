s=input()=='';b=[0]
for i in input():t=i=='.';b+=[b[-1]+1-t*2];s+=t
print(min([i+s for i in b]))