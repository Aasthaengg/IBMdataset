from collections import Counter

N = int(input())
cnt_list = Counter(input())
mod = 10**9+7
total = 1

for v in cnt_list.values():
    total = (total*(v+1))%mod
print(total-1)