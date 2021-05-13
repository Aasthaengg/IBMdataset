a=1;d=eval('1'+'0'*18)
for i in open(0).read().split()[1:]:a=min(a*int(i),d+1)
print([a,-1][a>d])