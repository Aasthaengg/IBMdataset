import collections
n = int(input())
a = list(input().split())
cnt = collections.Counter(a)
c = 0
for key, value in cnt.items():
    while int(key) != value:
        value -= 1
        c += 1
        if value == 0:
            break
print(c)

