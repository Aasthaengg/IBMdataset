n = int(input())
lis = list(input().split())
dic = {}
for a in lis:
  if a in dic:
    dic[a] += 1
  else:
    dic[a] = 1
count = 0
for b in dic.keys():
  count += 1
if count == 3:
  print("Three")
else:
  print("Four")