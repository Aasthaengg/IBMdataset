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
s,t = map(str,input().split())

for i in range(n):
	print(s[i], end="")
	print(t[i], end="")