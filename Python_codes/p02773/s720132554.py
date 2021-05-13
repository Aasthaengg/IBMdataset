from collections import defaultdict
N = int(input())
dic = defaultdict(lambda:0)
for _ in range(N):
    key = input()
    dic[key] += 1

maxnum = max(dic.values())
collection = []
for key, value in dic.items():
    if value == maxnum:
        collection.append(key)

collection.sort()
for word in collection:
    print(word)