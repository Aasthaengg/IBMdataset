S=input()
T=["KIHBR","KIHBRA","KIHBAR","KIHBARA",
  "KIHABR","KIHABRA","KIHABAR","KIHABARA",
  "AKIHBR","AKIHBRA","AKIHBAR","AKIHABRA",
  "AKIHABR","AKIHABRA","AKIHABAR","AKIHABARA"]
ans=0
for i in range(16):
  if(S==T[i]):
    ans=1
if(ans):
  print("YES")
else:
  print("NO")

