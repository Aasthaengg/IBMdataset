from collections import Counter
n = int(input())
a = list(map(int, input().split()))

a = Counter(a)
cnt = 0
for k, v in a.items():
    if k == v:
        continue
    elif k > v:
        cnt += v
    else:
        cnt += v - k

print(cnt)