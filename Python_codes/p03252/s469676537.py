from collections import defaultdict
 
S = list(input())
T = list(input())
ds = defaultdict(int)
dt = defaultdict(int)
cnt_s = []
cnt_t = []
for s, t in zip(S, T):
    ds[s] += 1
    dt[t] += 1
    cnt_s.append(ds[s])
    cnt_t.append(dt[t])
print('Yes' if cnt_s == cnt_t else "No")