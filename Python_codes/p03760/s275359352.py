#
from collections import Counter

k = input()
p = input()
d = len(k)
f = len(p)
g=""
diff = abs(d-f)

if d>f :
     d = d-diff
     g = k[d:len(k)]
   
else:
    f = f-diff
    g=p[f:len(p)]


r=""
i = 0
for i in range(d):
    r += "".join(k[i]+p[i])
    #print(r)
    
print(r+g)