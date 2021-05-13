from collections import defaultdict
dic = defaultdict(int)

for i in range(3):
    p,q = map(int,input().split())
    dic[p] += 1
    dic[q] += 1
#print(dic)
L = []
for v in dic.values():
    L.append(v)

odd = [x%2 ==1 for x in L]
even = [x%2 ==0 for x in L]

if sum(odd) == 2 or sum(even) == 4:
    print("YES")
else:
    print("NO")