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

a = i()
b = i()
c = i()
x = i()

ans = 0
for i in range(a+1):
	for j in range(b+1):
		for k in range(c+1):
			if x == 500*i + 100*j + 50*k:
				ans += 1
print(ans)