S = input().rstrip()
T = input().rstrip()
from collections import defaultdict
s2t = defaultdict(int)
t2s = defaultdict(int)
for s,t in zip(S,T):
    if (s2t[s] != 0 and s2t[s] != t) or (t2s[t] != 0 and t2s[t] != s):
        print('No')
        exit()
    s2t[s] = t
    t2s[t] = s
print('Yes')