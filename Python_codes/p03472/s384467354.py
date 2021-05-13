import math
import bisect

N, H = map(int, input().split())

alist = []
blist = []

for n in range(N):
    a, b = map(int, input().split())
    alist.append(a)
    blist.append(b)

a_max = max(alist)

b_th_list = []
for b in blist:
    if b > a_max:
        b_th_list.append(b)

num_th = len(b_th_list)
H_res = H - sum(b_th_list)

if H_res <= 0:
    b_th_list.sort(reverse=True)
    sum_d = 0
    ans = 0
    for b in b_th_list:
        ans += 1
        sum_d += b
        if sum_d >= H:
            break
    print(ans)

else:
    num_cut = math.ceil(H_res/a_max)
    print(num_cut + num_th)
