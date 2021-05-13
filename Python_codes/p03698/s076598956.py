import collections 
s = input()
s_collection = collections.Counter(s)

flag = True
for value in s_collection.values():
  if value > 1:
    flag = False

if flag:
  print("yes")
else:
  print("no")