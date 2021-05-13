import math 
import collections

N = int(input())
String = []
for i in range (0, N):
	S = str(input())
	S = sorted(S)
	V = str(S[0])
	for j in range (1, 10):
		V = V+str(S[j])
	String.append(V)
    
cnt = collections.Counter()
for word in String:
	cnt[word] += 1

V = cnt.most_common()

count = 0

for i in range (0, len(V)):
	count+=math.comb(V[i][1], 2)
    
print(count)