import itertools
n = int(input())
#
# lst = []
# for v in itertools.permutations(range(1,n+1),n):
#     tmp = 0
#     for i in range(n):
#         tmp += (i+1) % v[i]
#     lst.append(tmp)
# print(max(lst))
ans = 0
for i in range(1,n):
    ans += i
print(ans)