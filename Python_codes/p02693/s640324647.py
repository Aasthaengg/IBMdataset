k = int(input())
a, b = map(int, input().split())


for i in range(a, b+1):
	if b-a >= k:
		print("OK")
		break
	elif i % k == 0:
		print("OK")
		break
	elif (i % k != 0) and (i == b):
		print("NG")
		break