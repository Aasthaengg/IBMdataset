S = input()
cnt = 0
for i in range(0, len(S)):
	if S[i] == 'x': cnt += 1
if cnt < 8: print('YES')
else: print('NO')