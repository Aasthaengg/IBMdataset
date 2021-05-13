s = list(input())
t = list(input())
l = len(s)
sl = [[] for _ in range(26)]
for i in range(l):
	j = ord(s[i])-97
	sl[j].append(i)
sord = [[-1 for _ in range(l)] for _ in range(26)]
checksord = [0 for _ in range(26)]
for i in range(26):
	for j in range(len(sl[i])):
		cnt = sl[i][j]
		for q in range(checksord[i], cnt):
			sord[i][q] = cnt
		checksord[i] = cnt

for i in range(26):
	for j in range(l):
		if (sl[i] != []) & (sord[i][j] == -1):
			sord[i][j] = sl[i][0] + l

#print(sord)

j = ord(t[0])-97
if sl[j] == []:
	ans = -1
else: 
	ans = sl[j][0]

if ans != -1:
	for i in range(1, len(t)):
		j = ord(t[i])-97
		if sl[j] == []:
			ans = -1
			break
		else:
			w = ans % l
			ans = ans - w + sord[j][w]
			#print(ans)

if ans == -1:
	print(ans)
else:
	print(ans+1)
