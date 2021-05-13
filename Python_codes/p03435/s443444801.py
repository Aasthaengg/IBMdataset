l=[]
for i in range(3):
  l.append(list(map(int,input().split())))
ch=[]
for i in l:
  ch.append([i[0]-i[1],i[1]-i[2]])
if ch[0]==ch[1] and ch[1]==ch[2]:
  print("Yes")
else:
  print("No")