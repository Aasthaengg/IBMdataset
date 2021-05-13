N = int(input())

S = []

import collections

for i in range (0, N):
	S.append(str(input()))

S = sorted(S)
cnt = collections.Counter()

for word in S:
	cnt[word] += 1
    
mostCommon = cnt.most_common()

D = mostCommon[0][1]
print(mostCommon[0][0])
for i in range(1, len(set(S))):
	if mostCommon[i][1] == D:
		print(mostCommon[i][0])
	else:
		exit()