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

s = i()
if len(s) == len(set(s)):
	print('yes')
else:
	print('no')
