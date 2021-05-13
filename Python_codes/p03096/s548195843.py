d={i:0for i in range(1<<18)};c=0;r=1
for _ in[0]*int(input()):m=int(input());r+=d[m]*(c!=m);d[m]=r;c=m
print(r%(10**9+7))