from collections import Counter

lis = list(input().split())

a = Counter(lis)

for k, v in a.items():
    if a[k] == 1:
        print(k)