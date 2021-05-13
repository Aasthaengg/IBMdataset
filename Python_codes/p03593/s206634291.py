from collections import Counter
import math

h, w = map(int,input().split())
a = [list(input()) for _ in range(h)]

c=Counter(sum(a,[]))

if h%2==0 and w%2==0:
    g1=0
    g2=0
    g4=(h//2)*(w//2)
elif h%2==1 and w%2==0:
    g1=0
    g2=w//2
    g4=(h//2)*(w//2)
elif h%2==0 and w%2==1:
    g1=0
    g2=h//2
    g4=(h//2)*(w//2)
else:
    g1=1
    g2=(h//2)+(w//2)
    g4=(h//2)*(w//2)

g1_cnt=0
g2_cnt=0
g4_cnt=0

for key in c:
    if c[key]%4==1:
        g1_cnt+=1
        g4_cnt+=c[key]//4
    elif c[key]%4==2:
        g2_cnt+=1
        g4_cnt+=c[key]//4
    elif c[key]%4==2:
        g1_cnt+=1
        g2_cnt+=1
        g4_cnt+=c[key]//4
    else:
        g4_cnt+=c[key]//4

# print(g1,g2,g4)

# print(g1_cnt,g2_cnt,g4_cnt)

flag=False
if g1==g1_cnt:
    if g2==g2_cnt and g4==g4_cnt:
        flag=True
    elif g2_cnt<g4_cnt and g2>g4 and g2*2+g4*4==g2_cnt*2+g4_cnt*4:
        flag=True

print('Yes' if flag else 'No')
