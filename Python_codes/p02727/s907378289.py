x,y,a,b,c = map(int, input().split(" "))
plist= sorted(list(map(int, input().split(" "))),reverse=True)[0:x]
qlist= sorted(list(map(int, input().split(" "))),reverse=True)[0:y]
rlist= sorted(list(map(int, input().split(" "))),reverse=True)

plist.extend(qlist)
plist.sort()
n = min(x+y,len(rlist))
i = 0

while i < n and rlist[i]>plist[i]:
  i += 1
if i == 0:
  print(sum(plist))
else:
  print(sum(plist[i:x+y])+sum(rlist[0:i]))
