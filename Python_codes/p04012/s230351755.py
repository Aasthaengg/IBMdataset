w=input()
alphabet=[chr(ord('a')+i) for i in range(25)]
count=1
for i in range(25):
  count=count*(1-(w.count(alphabet[i])%2))
if count%2==1:
  print('Yes')
else:
  print('No')