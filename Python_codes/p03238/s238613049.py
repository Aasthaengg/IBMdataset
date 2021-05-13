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

n = i()
if n == 1:
	print("Hello World")
else:
	a = i()
	b = i()
	print(a+b)