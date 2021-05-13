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

a,b = i2()
cnt = 0
for i in range(a,b+1):
	memo = str(i)
	if memo[0] == memo[4] and memo[1] == memo[3]:
		cnt += 1
print(cnt)