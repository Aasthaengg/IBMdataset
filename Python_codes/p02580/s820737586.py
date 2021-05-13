import sys
H, W, M = map(int, input().split())
h_list, w_list = [0]*H, [0]*W
check = set()
for _ in range(M):
    h, w = map(int, input().split())
    check.add((h-1, w-1))
    h_list[h-1] += 1
    w_list[w-1] += 1
h_max, w_max = max(h_list), max(w_list)
h_bom = [i for i in range(H) if h_list[i]==h_max]
w_bom = [i for i in range(W) if w_list[i]==w_max]
for h in h_bom:
    for w in w_bom:
        if not (h, w) in check:
            print(h_max+w_max)
            sys.exit()
print(h_max+w_max-1)