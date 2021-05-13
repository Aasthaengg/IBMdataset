from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
cnt = defaultdict(int)
data = []
for i in range(n):
    cnt[a[i]] += 1

if sum(v >= 2 for v in cnt.values()) < 2:
    print(0)
elif cnt[max(cnt.keys())] >= 4:
    print(max(cnt.keys()) ** 2)

else:
    for k, v in cnt.items():
        if v >= 2:
            data.append(k)
    data.sort(reverse = True)
    print(data[0] * data[1])