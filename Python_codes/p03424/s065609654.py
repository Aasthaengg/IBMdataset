from collections import Counter
n = int(input())
s = list(input().split())

c = Counter(s)

if len(list(c.keys())) == 3:
    print('Three')
else:
    print('Four')