from collections import Counter
n = int(input())
l = []
for i in range(n):
   l.append(int(input()))
lcnt = Counter(l)
l_value = list(lcnt.values())
for i in range(len(l_value)):
  if l_value[i]%2 == 0:
    l_value[i] = 0
  else:
    l_value[i] = 1    
print(sum(l_value))
