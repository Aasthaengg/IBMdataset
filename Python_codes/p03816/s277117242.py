import collections
n = int(input())
a = list(map(int, input().split()))

counter = collections.Counter(a)
count = 0
for k, v in counter.items():
    if v >= 2:
        count += v-1
if count % 2 == 0:
    print(n-count)
else:
    print(n-count - 1)
