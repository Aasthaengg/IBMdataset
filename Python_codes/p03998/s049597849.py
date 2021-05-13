Sa=input()
Sb=input()
Sc=input()
cur=0
while True:
  if cur==0:
    if len(Sa)==0:
      print("A")
      exit()
    cur=ord(Sa[0])-ord("a")
    Sa=Sa[1:]
  elif cur==1:
    if len(Sb)==0:
      print("B")
      exit()
    cur=ord(Sb[0])-ord("a")
    Sb=Sb[1:]
  else:
    if len(Sc)==0:
      print("C")
      exit()
    cur=ord(Sc[0])-ord("a")
    Sc=Sc[1:]
