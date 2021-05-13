import re
a=0
for m in re.findall('(<*)(>*)',input()):u,v=map(len,m);a+=(u*u-u+v*v-v)//2+max(u,v)
print(a)