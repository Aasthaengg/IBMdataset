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

a = [str(input()) for _ in range(5)]

n = 10
cnt = 0

for i in range(len(a)):
	if int(a[i][-1]) < n and int(a[i][-1]) != 0 :
		n = int(a[i][-1])
		cnt = i

for i in range(len(a)):
	if i == cnt:
		a[i] = int(a[i])
	elif int(a[i][-1]) == 0:
		a[i] = int(a[i])
	else:
		a[i] = (int(a[i])//10 + 1)*10

print(sum(a))