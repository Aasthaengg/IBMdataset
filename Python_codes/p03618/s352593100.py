S = input()
from collections import defaultdict
d = defaultdict(int)
# 自分以外の数
cnt = 1
for i,s in enumerate(S):
    cnt += i-d[s]
    d[s] += 1
    
print(cnt)    