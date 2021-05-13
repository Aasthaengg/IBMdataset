from collections import Counter
import sys
s = input()
n = len(s)

b = Counter(s)
c = list(b)
ssc = []
for i in range(n):
    ssc.append(s[i])

ans = 114514191933-4

if len(b) == 1:
    print(0)
    sys.exit()

for l in c:
    a = 0
    s2 = ssc
    ss = []
    for i in range(n-1):
        k = len(s2)
        for j in range(k-1):
            if s2[j] == l or s2[j+1] == l:
                ss.append(l)
            else:
                ss.append(s2[j+1])
                
        d = Counter(ss)
        if d[l] == k-1:
            ans = min(n-len(ss),ans)
            break
            
        s2 = ss
        ss = []
    
print(ans)