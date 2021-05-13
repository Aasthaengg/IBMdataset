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

a = s()
b = s()

sample = ""
for i in range(len(a)):
	a = a[-1] + a[0:-1]
	if a == b:
		print("Yes")
		exit()
print("No")