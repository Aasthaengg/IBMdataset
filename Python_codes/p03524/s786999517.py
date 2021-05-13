import collections
s = list(input())
s = collections.Counter(s)
a = s["a"]
b = s["b"]
c = s["c"]

if max(a,b,c) - min(a,b,c) <= 1:
  print("YES")
else:
  print("NO")