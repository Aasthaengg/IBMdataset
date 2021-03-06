import sys

#f = open("test.txt", "r")
f = sys.stdin

num_rank = 14
s_list = [False] * num_rank
h_list = [False] * num_rank
c_list = [False] * num_rank
d_list = [False] * num_rank

n = f.readline()

n = int(n)

for i in range(n):
	[suit, num] = f.readline().split()
	num = int(num)
	if suit == "S":
		s_list[num] = True
	elif suit == "H":
		h_list[num] = True
	elif suit == "C":
		c_list[num] = True
	else:
		d_list[num] = True

for i in range(1, num_rank):
	if not s_list[i]:
		print("S " + str(i))
for i in range(1, num_rank):
	if not h_list[i]:
		print("H " + str(i))
for i in range(1, num_rank):
	if not c_list[i]:
		print("C " + str(i))
for i in range(1, num_rank):
	if not d_list[i]:
		print("D " + str(i))