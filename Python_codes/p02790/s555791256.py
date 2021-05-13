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

a,b = i2()
a1 = ""
b1 = "" 
for i in range(b):
	a1 += str(a)
for i in range(a):
	b1 += str(b)

if a1 < b1:
	print(a1)
else:
	print(b1)