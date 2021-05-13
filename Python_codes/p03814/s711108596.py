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
	if s[i] == "A":
		m1 = i
		break
for i in range(-1,-len(s)-1,-1):
	if s[i] == "Z":
		m2 = i
		break
print(len(s) + m2 - m1 + 1)