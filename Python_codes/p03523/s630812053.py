S = input()

T = "AKIHABARA"
cand = [
  "KIHBR",
  "KIHBAR",
  "KIHABAR",
  "KIHABR",
  "AKIHABAR",
  "AKIHBAR",
  "AKIHABR",
  "AKIHBR",
  "KIHBRA",
  "KIHBARA",
  "KIHABARA",
  "KIHABRA",
  "AKIHABARA",
  "AKIHBARA",
  "AKIHABRA",
  "AKIHBRA",
]
print("YES" if S in cand else "NO")