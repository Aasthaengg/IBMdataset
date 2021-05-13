n = int(input())
s = str(input())
cnt = 0
def f(x):
	tgt = [ x[0], x[1], x[2] ]
	now = 0
	global n
	for i in range(n):
		if s[i] == tgt[now]: now += 1
		if now == 3: return True
	return False
for i in range(1000):
	if len(str(i)) == 1: t = "00"+str(i)
	elif len(str(i)) == 2: t = "0"+str(i)
	else: t = str(i)
	if f(t): cnt += 1
print(cnt)