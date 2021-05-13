S = input()
T = 'CODEFESTIVAL2016'

cnt = 0
for i in range(len(T)):
	if S[i:i+1]!=T[i:i+1]:
		cnt += 1

print(cnt)