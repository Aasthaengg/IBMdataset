A = list(input())
n = len(A)

str_cnt = {}
for a in A:
    if a in str_cnt:
        str_cnt[a] += 1
    else:
        str_cnt[a] = 1
# print(str_cnt)
zen = n * (n - 1) // 2 + 1

for k in str_cnt:
    num = str_cnt[k]
    if num > 1:
        zen -= num * (num - 1) // 2
print(zen)
