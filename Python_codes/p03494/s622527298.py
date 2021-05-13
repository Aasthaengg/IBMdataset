# ABC_081_B_Shift_only.py
N = int(input())
a = list(map(int, input().split()))
count = 0
while True:
	flag = 0
	for i in range(0, N):
		Ai = a[i]
		if Ai % 2 == 1:
			flag = 1
	if flag == 1:
		break
	for i in range(0, N):
		a[i] = a[i]//2
	count += 1
print(count)