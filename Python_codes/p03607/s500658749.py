n = int(input())
a = [int(input()) for _ in range(n)]

from collections import Counter

c = Counter(a)
print(sum([1 for num,cnt in c.items() if cnt%2==1]))