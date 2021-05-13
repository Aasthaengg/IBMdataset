from collections import Counter
n = int(input())
a = [int(input()) for i in range(n)]
b = Counter(a).values()
c = [x for x in b if x % 2 != 0]
print(len(c))