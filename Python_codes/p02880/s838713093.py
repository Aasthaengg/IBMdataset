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

for i in range(1,10):
	if n%i == 0:
		if (n//i)%10 == n//i:
			print("Yes")
			exit()
print("No")