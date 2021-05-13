n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
l = [list(map(int, input().split())) for i in range(m)]
l.sort(key=lambda x: x[1], reverse=True)

res = 0
pos_1 = 0
pos_2 = 0
for _ in range(n):
    if pos_2 == m or a[pos_1] > l[pos_2][1]:
        res += a[pos_1]
        pos_1 += 1
    else:
        res += l[pos_2][1]
        l[pos_2][0] -= 1
        if l[pos_2][0] == 0:
            pos_2 += 1
 
print(res)

# d = []
# while l and len(d) <= n:
#     bc = l.pop(0)
#     d.extend([bc[1]]*bc[0])
# ret = 0
# for i in range(n):
#     if d and d[0] > a[0]:
#         ret += d.pop(0)
#     else:
#         ret += a.pop(0)
# print(ret)