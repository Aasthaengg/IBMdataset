from collections import Counter
a = Counter(list(map(int, input().split())))

for k, v in a.items():
    if v==1:
        print(k)
