from bisect import *
s = str(input())
K = int(input())
ls = len(s)
l = []
for i in range(ls):
  for j in range(i+1,i+K+2):
    l.append(s[i:j])

l = list(set(l))
l = sorted(l)
print(l[K-1])