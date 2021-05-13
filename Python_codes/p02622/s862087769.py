S = input()
T = input()

cnt = 0
for i in range(len(S)):
	if S[i] == T[i]:
		cnt = cnt
	else:
		cnt += 1
print(cnt)