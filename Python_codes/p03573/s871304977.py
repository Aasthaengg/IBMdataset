from collections import Counter
li = map(int, input().split())
cnts = Counter(li).most_common()
print(cnts[-1][0])
