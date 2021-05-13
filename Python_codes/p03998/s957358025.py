s=[]
for i in range(3):
  s.append(input())
member=["A","B","C"]
turn=0

while True:
  if s[turn]=="":
      winner=turn
      break
  if s[turn][0]=="a":
    next=0
  elif s[turn][0]=="b":
    next=1
  else:
    next=2
  s[turn]=s[turn][1:]
  turn=next

print(member[winner])
