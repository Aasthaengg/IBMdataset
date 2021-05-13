#AKIHABARA
S = input()
T = ["AKIHABARA",
     "AKIHABAR",
     "AKIHABRA",
     "AKIHBARA",
     "KIHABARA",
     "AKIHABR",
     "AKIHBAR",
     "KIHABAR",
     "AKIHBRA",
     "KIHABRA",
     "KIHBARA",
     "AKIHBR",
     "KIHABR",
     "KIHBAR",
     "KIHBRA",
     "KIHBR"]
for t in T:
    if t == S:
        print("YES")
        exit()
print("NO")