n = int(input())
la = [int(input()) for _ in range(n)]

dict_i = {}

for i, a in enumerate(la):
    dict_i[a] = i


m = 0
s = 0
j = -1
for a in range(1, n + 1):
    i = dict_i[a]
    if i > j:
        s += 1
        m = max(m, s)
    else:
        s = 1
    j = i

answer = n - m
print(answer)
