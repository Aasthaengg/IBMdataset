s = input().rstrip().split(' ')
a = int(s[0])
b = int(s[1])
c = int(s[2])
cnt = 0

for i in range(a,b+1):
	if c % i == 0:
		cnt = cnt + 1
		#print(str(i))

print(str(cnt))