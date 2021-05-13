from collections import Counter


n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
count = 0
for k, v in c.items():
    if k < v:
        count += (v - k)
    elif k > v:
        count += v
print(count)
