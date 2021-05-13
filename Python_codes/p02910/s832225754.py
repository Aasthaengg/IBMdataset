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

s = s()
for i in range(len(s)):
	if i%2 == 0 and s[i] not in ["R","U","D"]:
		print("No")
		exit()
	elif i%2 == 1 and s[i] not in ["L","U","D"]:
		print("No")
		exit()
print("Yes")