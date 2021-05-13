from collections import Counter
import bisect
import sys
s = input()
t = input()
sb = Counter(s)
tb = Counter(t)
S = len(s)
T = len(t)

for i in range(26):
    x = chr(i+97)
    
    if sb[x] == 0 and tb[x] >= 1:
        print(-1)
        sys.exit()
        
le = [[] for i in range(26)]
for i in range(S):
    le[ord(s[i]) - 97].append(i+1)
        
loop = 0
hasu = 0

for i in range(T):
    x = ord(t[i]) - 97
    c = bisect.bisect(le[x],hasu)
    if c == len(le[x]):
        loop += 1
        hasu = le[x][0]
    else:
        hasu = le[x][c]
        
print(loop*S + hasu)