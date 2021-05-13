N = int(input())
S = input()
table_e = []
count_e = 0
table_w = []
count_w = 0
for s in S:
    if s == 'E':
        count_e += 1
    else:
        count_w += 1
    table_e.append(count_e)
    table_w.append(count_w)
ans = float('inf')
for i in range(N):
    tmp = table_w[i - 1] if i else 0
    tmp += count_e - table_e[i]
    ans = min(ans, tmp)
print(ans)
