def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

d = i()
if d == 25:
	print("Christmas")
elif d == 24:
	print("Christmas Eve")
elif d == 23:
	print("Christmas Eve Eve")
else:
	print("Christmas Eve Eve Eve")
