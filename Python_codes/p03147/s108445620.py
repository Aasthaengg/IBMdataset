n = int(input())
H = list(map(int, input().split()))
count = 0

while any(h for h in H):
	count += 1
	flag = False
	for i, h in enumerate(H):
		if h:
			flag = True
			H[i] -= 1
		else:
			if flag == True:
				break
print(count)