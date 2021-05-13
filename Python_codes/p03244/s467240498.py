from collections import Counter
n = int(input())
l = list(map(int,input().split()))
l_o = l[::2]
l_g = l[1::2]
a = list(Counter(l_o).most_common())+[(0,0)]
c = list(Counter(l_g).most_common())+[(0,0)]

if a[0][0]==c[0][0]:
  s = a[0][1]+c[1][1]
  t = a[1][1]+c[0][1]
  x = max(s,t)
  print(n-x)
  
  
else:
  print(n-a[0][1]-c[0][1])