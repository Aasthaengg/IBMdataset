from collections import Counter
a = list(map(int, input().split()))
c = Counter(a).most_common()
print(c[-1][0])

