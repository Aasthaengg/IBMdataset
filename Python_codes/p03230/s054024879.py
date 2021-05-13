n = int(input())
ans = True
for k in range(1, 500):
    if n == k * (k - 1) / 2:
        ans = False
        break
if ans:
    print('No')
    exit()
print('Yes')
print(k)
val = 1
ans_list = [[] for _ in range(k)]
for i in range(k - 1):
    for j in range(i + 1, k):
        ans_list[i].append(val)
        ans_list[j].append(val)
        val += 1
for a in ans_list:
    print(*([len(a)] + a))