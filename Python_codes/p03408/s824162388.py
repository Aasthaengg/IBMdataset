from collections import Counter as C
n=int(input())
s=[input()  for i in  range(n)]
m=int(input())
t=[input()  for i in  range(m)]

sd=C(s)
td=C(t)

max=0
for k in sd:
  if sd[k]-td[k]>max:
    max=sd[k]-td[k]
print(max)