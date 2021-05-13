n = int(input())
a = list(map(int, input().split())) 
from collections import Counter
dic = Counter(a)
ans = 0
for k in dic:
    if dic[k] > k:
        ans += dic[k] - k
    if dic[k] < k:
        ans += dic[k]
print(ans)