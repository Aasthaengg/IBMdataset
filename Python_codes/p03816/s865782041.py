from collections import defaultdict
N, *A = map(int, open(0).read().split())
cnt = defaultdict(int)
csum = 0
for a in A:
    cnt[a] += 1
    csum += 1

dup = 0
for v in cnt.values():
    if v > 1:
        dup += v-1
        
if dup & 1:
    print(N-dup-1)
else:
    print(N-dup)