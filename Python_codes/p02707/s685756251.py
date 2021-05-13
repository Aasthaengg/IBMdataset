from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

for i in range(1, n + 1):
    if i in c:
        print(c[i])
    else:
        print(0)
