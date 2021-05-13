N = int(input())

TP = 0
HP = 0

for i in range(N):
	TC, HC = input().split()
	if TC > HC:
		TP += 3
	elif TC < HC:
		HP += 3
	else:
		TP += 1
		HP += 1

print(TP,HP)