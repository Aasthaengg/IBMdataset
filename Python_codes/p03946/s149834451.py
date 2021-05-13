from collections import defaultdict
n, t = [int(x) for x in input().split()]
a_list = [int(x) for x in input().split()]
d = defaultdict(int)
a_min = a_list[0]
p_max = 0
for i in range(1, n):
    if a_list[i] < a_min:
        a_min = a_list[i]
        continue
    p = a_list[i] - a_min
    if p >= p_max:
        d[p] += 1
        p_max = p
print(d[p_max])