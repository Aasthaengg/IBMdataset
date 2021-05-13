from itertools import product
import copy
H,W,K = map(int,input().split())
C_ary = [[_ for _ in input()] for j in range(H)]
patrn_h = []
patrn_w = []
cntup = 0
for i in product([0,1], repeat = H):
    patrn_h.append(i)
for i in product([0,1], repeat = W):
    patrn_w.append(i)
for i in patrn_h:
    for j in patrn_w:
        cnt = 0
        test_ary = copy.deepcopy(C_ary)
        for h in range(H):
            for w in range(W):
                if i[h] == 0 or j[w] == 0:
                    test_ary[h][w] = "."
            cnt += test_ary[h].count("#")
        if cnt == K:
            cntup += 1
print(cntup)