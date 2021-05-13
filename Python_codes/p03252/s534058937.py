a = input()
b = input()
dic = {}

for i in range(len(a)):
  if not b[i] in dic:
    dic[b[i]] = a[i]
  else:
    if dic[b[i]] != a[i]:
      print("No")
      quit()
  #print(dic)
c = list(dic.values())
d = set(c)
#print(c)
#print(d)
if len(c) == len(d):
  print("Yes")
else:
  print("No")