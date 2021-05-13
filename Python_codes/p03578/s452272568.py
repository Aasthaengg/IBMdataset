from collections import defaultdict
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
cnt_d, cnt_t = defaultdict(int), defaultdict(int)
for dif in d:
    cnt_d[dif] += 1

for t_dif in t:
    cnt_t[t_dif] += 1

for k, v in cnt_t.items():
    if v > cnt_d[k]:
        print("NO")
        exit()

print("YES")