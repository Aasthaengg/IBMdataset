S=input()
N=len(S)

cnt=0
pre=""
last=""

for str in S:
  str = pre +str
  if str==last:
    pre += str
  else:
    cnt +=1
    last=str
    pre=""
    
print(cnt)