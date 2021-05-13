N = int(input())
lremain = []
rremain = []

for i in range(N):
	S = input()
	left = 0
	right = 0
	for c in S:
		if c == "(":
			left += 1
		else:
			if left == 0:
				right += 1
			else:
				left -= 1
	if left == 0 and right == 0:
		continue
	lremain.append(left)
	rremain.append(right)

N = len(lremain)

if sum(lremain) != sum(rremain):
	print("No")
	exit()

head = 0
tail = 0
removei = set()
for i in range(N):
	if rremain[i] == 0:
		head += lremain[i]
		removei.add(i)
	if lremain[i] == 0:
		tail += rremain[i]
		removei.add(i)

lnr = []
for i in range(N):
	if not i in removei:
		lnr.append((lremain[i], rremain[i]))

N = len(lnr)
lnr.sort(key = lambda x: (x[1]-x[0]))

for i in range(N):
	if head < lnr[i][1]:
		print("No")
		exit()
	head -= lnr[i][1]
	head += lnr[i][0]

if head == tail:
	print("Yes")
else:
	print("No")
