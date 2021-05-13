s = input()
d = []
d.append("AKIHABARA")

d.append("AKIHABAR")
d.append("AKIHABRA")
d.append("AKIHBARA")
d.append("KIHABARA")

d.append("AKIHABR")
d.append("AKIHBRA")
d.append("AKIHBAR")
d.append("KIHBARA")
d.append("KIHABRA")
d.append("KIHBAR")

d.append("AKIHBR")
d.append("KIHABR")
d.append("KIHBAR")
d.append("KIHBRA")

d.append("KIHBR")
if s in d:
    print("YES")
else:
    print("NO")
