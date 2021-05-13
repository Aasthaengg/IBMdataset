n=int(input());a=[0];b=[0]
for i in input():t=i=='.';a+=[a[-1]+t];b+=[b[-1]+1-t*2];
print(min([i+a[n] for i in b]))