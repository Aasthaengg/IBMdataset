n = int(input())
d = list(map(int, input().split())) 
m = int(input())
t = list(map(int, input().split())) 

from collections import Counter

dc, tc = Counter(d), Counter(t)
ans = "YES"
for p in tc.keys():
    if tc[p] > dc[p]:
        ans = "NO"
 
print(ans)