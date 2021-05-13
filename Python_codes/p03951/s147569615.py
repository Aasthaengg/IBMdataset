n = int(input())
s = input()
t = input()

if s == t:
	print(n)
	exit()

for i in range(n):
	if s[i:] == t[:-i]:
		print(n + i)
		exit()
else:
	print(n * 2)