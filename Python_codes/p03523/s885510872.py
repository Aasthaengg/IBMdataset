import sys
def input():
	return sys.stdin.readline().strip()

S = input()

S_list = ["AKIHABARA", "AKIHABAR", "AKIHABRA", "AKIHABR", "AKIHBARA", "AKIHBAR", "AKIHBRA", "AKIHBR",
		  "KIHABARA", "KIHABAR", "KIHABRA", "KIHABR", "KIHBARA", "KIHBAR", "KIHBRA", "KIHBR"]

if S in S_list:
	print("YES")
else:
	print("NO")