n, c = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

re_lst = []
for i in reversed(range(n)):
    re_lst.append([abs(c-lst[i][0]), lst[i][1]])

r_accum = []
s = 0
for i in range(n):
    s += lst[i][1]
    r_accum.append(s)

l_accum = []
s = 0
for i in range(n):
    s += re_lst[i][1]
    l_accum.append(s)

r_max = 0
r_max_lst = []
for i in range(n):
    r_max = max(r_max, r_accum[i] - lst[i][0])
    r_max_lst.append(r_max)
    
l_max = 0
l_max_lst = []
for i in range(n):
    l_max = max(l_max, l_accum[i] - re_lst[i][0])
    l_max_lst.append(l_max)

rd_max = 0
for i in range(n-1):
    pt = r_accum[i] - 2*lst[i][0]
    pt += l_max_lst[(n-1)-i-1]
    if pt > rd_max:
        rd_max = pt
            

ld_max = 0
for i in range(n-1):
    pt = l_accum[i] - 2*re_lst[i][0]
    pt += r_max_lst[(n-1)-i-1]
    if pt > ld_max:
        ld_max = pt

print(max(r_max, l_max, rd_max, ld_max))