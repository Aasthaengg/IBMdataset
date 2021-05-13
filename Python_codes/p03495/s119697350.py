from collections import OrderedDict

N, K =map(int, input().split())
a = list(map(int, input().split()))
p = OrderedDict()
for i in a:
  if i not in p:
    p[i] = 1
  else:
    p[i] +=1
#print(p)
p_rev = OrderedDict(
    sorted(p.items(), key=lambda x: x[1])
)
#print(p_rev)
#print(len(p_rev))
count = 0
sum = 0
for i in p_rev.values():
  if len(p_rev) - count > K:
    sum += i
    count += 1
  else:
    break
print(sum)