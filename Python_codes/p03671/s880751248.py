# -*- coding: utf-8 -*-

a,b,c=[int(i) for i in input().rstrip().split()]
#-----
sum_abc = a+b+c

ans=10000*2
for i in [a,b,c]:
    ans = min(ans, (sum_abc - i))

print(ans)
