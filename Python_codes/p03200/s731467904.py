s = input()
n = len(s)

cnt =  0
cnt_W = 0
for i in range(n):
	if s[i] == 'W':
		cnt += i
		cnt_W += 1

res = cnt - (cnt_W - 1) * cnt_W // 2
print(res)
