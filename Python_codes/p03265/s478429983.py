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


x1,y1,x2,y2= i2()
x3 = x2 - (y2 - y1)
y3 = y2 + (x2 - x1)
x4 = x3 - (y3 - y2)
y4 = y3 + (x3 - x2)
print(x3,y3,x4,y4)