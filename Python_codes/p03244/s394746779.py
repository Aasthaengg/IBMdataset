import collections

N = int(input())
V = list(map(int, input().split()))

even = V[::2]
odd = V[1::2]

even_c = collections.Counter(even)
odd_c = collections.Counter(odd)

even_max1_num = 0
even_max1_cnt = 0
even_max2_num = 0
even_max2_cnt = 0
for k, v in even_c.items():
    if v > even_max1_cnt:
        even_max2_cnt = even_max1_cnt
        even_max2_num = even_max1_num
        even_max1_cnt = v
        even_max1_num = k
    elif v > even_max2_cnt:
        even_max2_cnt = v
        even_max2_num = k

odd_max1_num = 0
odd_max1_cnt = 0
odd_max2_num = 0
odd_max2_cnt = 0
for k, v in odd_c.items():
    if v > odd_max1_cnt:
        odd_max2_cnt = odd_max1_cnt
        odd_max2_num = odd_max1_num
        odd_max1_cnt = v
        odd_max1_num = k
    elif v > odd_max2_cnt:
        odd_max2_cnt = v
        odd_max2_num = k

ans = 0
if even_max1_num == odd_max1_num:
    if even_max1_cnt == odd_max1_cnt:
        if even_max2_cnt > odd_max2_cnt:
            ans = N-(even_max2_cnt+odd_max1_cnt)
        else:
            ans = N-(even_max1_cnt+odd_max2_cnt)
    elif even_max1_cnt > odd_max1_cnt:
        ans = N-(even_max1_cnt+odd_max2_cnt)
    else:
        ans = N-(even_max2_cnt+odd_max1_cnt)
else:
    ans = N-(even_max1_cnt+odd_max1_cnt)
print(ans)
