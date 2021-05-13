from collections import defaultdict
N,*A = map(int,open(0).read().split())
d = defaultdict(int) #初期値１
for a in A:
    d[a] ^= 1 #0と1を反転
print(sum(d.values())) 
