n = int(input())
s = input()
t = input()
u = []
flg = 0
mod = 10**9+7
for i in range(n):
	if s[i] == t[i]:
		u.append(1)
	else:
		if flg == 1:
			u.append(0)
			flg = 0
		else:
			flg = 1
if u[0] == 1:
	ans = 3
else:
	ans = 6
for i in range(len(u)-1):
	if u[i] == 1 and u[i+1] == 1:
		ans *= 2
	elif u[i] == 1 and u[i+1] == 0:
		ans *= 2
	elif u[i] == 0 and u[i+1] == 1:
		continue
	else:
		ans *= 3
	ans %= mod
print (ans)
