s = input()
n = len(s)

target = 'keyence'

for i in range(n):
	for j in range(i, n):
		res = s[:i] + s[j:]
		if res == target:
			print('YES')
			exit()

print('NO')