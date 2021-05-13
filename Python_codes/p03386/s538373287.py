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

a,b,k = i2()
if b - (a-1) <= 2*k:
	for i in range(a,b+1):
		print(i)
else:
	for i in range(k):
		print(a+i)
	for i in range(-k+1,1):
		print(b+i)