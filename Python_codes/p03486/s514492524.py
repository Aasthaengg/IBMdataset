s = list(input())
s.sort()

t = list(input())
t.sort(reverse =True)

list1 = [s,t]
list1.sort()
if list1[0] == t:
  print('No')
else:
  print('Yes')