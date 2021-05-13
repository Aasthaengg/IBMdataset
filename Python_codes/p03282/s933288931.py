s = input()
k = int(input())
ok = True
char = '1'
for i in range(k):
	if s[i] != '1':
		ok = False 
		char = s[i]
		break
if ok:
	print(1)
else:
	print(char)
