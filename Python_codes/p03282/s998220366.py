import sys
s = input()
n = int(input())
cnt = 0
if n == 1:
	print(s[0])
	sys.exit()
for i in s:
	if i == '1':
		cnt += 1
	else:
		break
if n <= cnt:
	print(1)
	sys.exit()
	
for i in s:
	if i != '1':
		print(i)
		sys.exit()
print(1)