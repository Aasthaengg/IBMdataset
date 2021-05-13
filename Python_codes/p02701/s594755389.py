n = int(input())
str_list = [input() for _ in range(n)]

from collections import Counter

c = Counter(str_list)
print(len(c))
