A,B = map(int,input().split())
cnt = 0
for i in range(B-A+1):
	tmp = A+i
	tmp = list(str(tmp))
	l = ''.join(tmp)
	if l == l[::-1]:
		cnt += 1
print(cnt)