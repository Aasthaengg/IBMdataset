from collections import defaultdict

n = int(input())
data_1 = defaultdict(int)
data_2 = defaultdict(int)
v = list(map(int, input().split()))
if len(set(v)) == 1:
    print(n // 2)
    exit()
for i in range(n):
    if i % 2 == 0:
        data_1[v[i]] += 1
    else:
        data_2[v[i]] += 1
data_1 = sorted(data_1.items(), key = lambda x: x[1],reverse = True)
data_2 = sorted(data_2.items(), key = lambda x: x[1],reverse = True)

ans = n - data_1[0][1] - data_2[0][1]
if data_1[0][0] == data_2[0][0]:
    ans = n - max(data_1[0][1] + data_2[1][1], data_1[1][1] + data_2[0][1])
print(ans)
