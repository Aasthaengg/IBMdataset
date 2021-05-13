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

h,w = i2()
a = ""
for _ in range(w+2):
	 a += "#"
print(a)
b = "#"
for i in range(h):
	c = s()
	b += c + "#"
	print(b)
	b = "#"
print(a)
