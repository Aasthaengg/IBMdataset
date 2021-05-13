def i():
	return str(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

s = list(i())
s.sort()

for i in range(len(s)-1):
	if s[i] == s[i+1]:
		print('no')
		exit()
print('yes')
