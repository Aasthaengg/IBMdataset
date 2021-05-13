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

ans = 0
cnt = 0
for i in range(len(s)):
	if cnt == 0:
		if s[i] in ["A", "T", "G", "C"]:
			cnt += 1
			if i == len(s)-1:
				ans = max(ans, cnt)
	elif cnt >= 1:
		if s[i] in ["A", "T", "G", "C"]:
			cnt += 1
			if i == len(s)-1:
				ans = max(ans,cnt)
		else:
			ans = max(ans,cnt)
			cnt = 0
print(ans)