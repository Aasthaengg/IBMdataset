import re
a=0
for m in re.findall('(<*)(>*)',input()):u,v=map(len,m);a-=(u*~u+v*~v)//2+min(u,v)
print(a)