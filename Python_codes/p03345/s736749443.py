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

a,b,c,k = i2()
if k%2 == 0:
	print(a - b)
else:
	print(b - a)