n, k = map(int,input().split(" "))
nl = list(map(int,input().split(" ")))
nl.sort()

for i in range(k):
  if not nl:
    break
  else:
  	nl.pop()
if not nl:
  print("0")
else:
  print(sum(nl))