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

cnt = 0
ans = 0
for j in range(1,n+1,2):
	for i in range(1,j+1):
		if j%i == 0:
			cnt += 1
	if cnt == 8:
		ans += 1
	cnt = 0
print(ans)