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
m1 = -1
for i in range(len(s)):
	if s[i] == "A" and m1 == -1:
		m1 = i
	if s[i] == "Z":
		m2 = i
	
print(m2 - m1 + 1)