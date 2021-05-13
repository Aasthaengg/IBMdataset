A,B,C = (int(x) for x in input().split())

list = [A, B, C]
import collections

count = collections.Counter(list)
keys = [k for k, v in count.items() if v== 1]
print(keys[0])
