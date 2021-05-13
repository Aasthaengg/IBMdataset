S =input()
T =input()

answer = len(T)
for i in range(len(S)-len(T)+1):
#	print(S[i:i + len(T)])
	count = 0
	for j in range(len(T)):
		if S[i + j] != T[j]:
			count = count + 1
	if count < answer:
		answer = count
print(answer)