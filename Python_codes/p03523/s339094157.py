s = input()
l = ["AKIHABARA","KIHABARA","AKIHBARA","AKIHABRA","AKIHABAR"]
l1 = ["KIHBR"]
l2 = ["AKIHBR","KIHABR","KIHBAR","KIHBRA"]
l3 = ["AKIHABR","AKIHBAR","AKIHBRA","KIHABRA","KIHABAR","KIHBARA"]
if s in l or s in l1 or s in l2 or s in l3:
  print("YES")
else:
  print("NO")