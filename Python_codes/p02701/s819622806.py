import collections
N = int(input())
item = []
for i in range(N):
    item.append(input())
item_count=collections.Counter(item)
print(len(item_count))
