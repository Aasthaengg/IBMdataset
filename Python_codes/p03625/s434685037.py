import collections
N = int(input())
l = list(map(int,input().split()))
c = collections.Counter(l)
dic = sorted(c.items(), reverse=True)
r = []
for j in dic:
    k = j[0]
    v = j[1]
    if v >= 4:
    	r.append(k)
    	r.append(k)
    elif v >= 2:
    	r.append(k)
    if len(r) >= 2:
      print(r[0]*r[1])
      exit()
print(0)