from collections import Counter
l = [int(i) for i in input().split()]

c = Counter(l)

print(c.most_common()[1][0])

