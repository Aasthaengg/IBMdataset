from collections import defaultdict
dic = defaultdict(int)

sl = list(input())
dic["a"] = 0
dic["b"] = 0
dic["c"] = 0
for s in sl:
    dic[s] += 1

if max(dic.values()) - min(dic.values()) <= 1:
    print("YES")
else:
    print("NO")

