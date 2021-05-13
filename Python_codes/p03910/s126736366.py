n = int(input())
"""
全探索→200点
"""
cnt = 1
while True:
	t = cnt*(cnt-1)//2
	if n < t:
		break
	cnt += 1
s = cnt*(cnt-1)//2-n
for i in range(1, cnt):
	if i != s:
		print(i)
