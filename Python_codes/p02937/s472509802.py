from collections import defaultdict
import copy
import sys
s = input()
n_s = len(s)
t = input()
n_t = len(t)

chr_firstind = defaultdict(lambda:-1)
chr_nextind = defaultdict(lambda:-1)
i_to_chr_nextind = [0] * n_s
for i in range(n_s-1,-1,-1):
    chr_firstind[s[i]] = i
    i_to_chr_nextind[i] = copy.copy(chr_nextind)
    chr_nextind[s[i]] = i 

first_target = t[0]
previous_ind = chr_firstind[first_target]
if previous_ind == -1:
    print(-1)
    sys.exit()
if n_t == 1:
    print(previous_ind+1)
    sys.exit()
s_used = 0
for i in range(1,n_t):
    # 一つ前のtarget_indを使って、次のtargetのs内でのindexを求める
    d = i_to_chr_nextind[previous_ind]
    next_ind = d[t[i]]
    if next_ind == -1:
        s_used += 1
        next_ind = chr_firstind[t[i]]
        if next_ind == -1:
            print(-1)
            sys.exit()
    previous_ind = next_ind
print(n_s*s_used+previous_ind+1)


