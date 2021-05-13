S = str(input())

count = 0

for i in range (0, len(S)):
	if S[i] == 'W':
		count+=1

choma = 0

for i in range (0, len(S)):
	if S[i] == 'W':
		choma+=(i+1)

if count*(count+1)/2 < choma:
	print(int(choma-count*(count+1)/2))
else:
	print(0)