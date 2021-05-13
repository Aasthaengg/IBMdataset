from collections import Counter
s=input()
t=input()

sc=Counter(s)
tc=Counter(t)
if len(sc)!=len(tc):
  print("No")
else:
  for s1,t1 in zip(sorted(sc.items(),key=lambda i: i[1]),sorted(tc.items(),key=lambda i: i[1])):
    if s1[1]!=t1[1]:
      print("No")
      break
  else:
    print("Yes")