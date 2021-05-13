n = int(input())
s_list = []
for _ in range(n):
    s_list.append(input())
m = int(input())
t_list = []
for _ in range(m):
    t_list.append(input())
    
# print(s_list)
# print(t_list)

st_set = set(s_list + t_list)
# print(st_set)

ans = 0
for st in st_set:
    # print(s_list.count(st))
    # print(t_list.count(st))
    # print(f"{s_list.count(st)} {t_list.count(st)}")
    ans = max(ans, s_list.count(st) - t_list.count(st))

print(ans)