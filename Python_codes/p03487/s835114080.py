from collections import Counter
n = int(input())
A = Counter(list(map(int,input().split())))
keys,counts = zip(*A.most_common())
total = 0
for key,count in zip(keys,counts):
    if key > count:
        total += count
    else:
        total += count-key
print(total)