import collections
n = int(input())
a = [int(input()) for _ in range(n)]
result = 0
cnt = collections.Counter(a)
for i in cnt.values():
    if i % 2 == 1:
        result += 1

print(result)