s = int(input())
k = input()
if len(k) > s:
	print("%s..." % k[:s])
else:
	print(k)