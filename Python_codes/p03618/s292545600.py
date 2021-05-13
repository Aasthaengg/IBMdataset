from collections import Counter
a = input()
c = len(a)*(len(a)-1)//2
for i in Counter(a).values():
  c -= i*(i-1)//2
print(c+1)