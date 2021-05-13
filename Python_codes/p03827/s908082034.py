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
s = s()
cnt = 0
ans = 0

for i in range(n):
	if s[i] == "I":
		cnt += 1
	else:
		cnt -= 1
	if cnt >= ans:
		ans = cnt
print(ans)