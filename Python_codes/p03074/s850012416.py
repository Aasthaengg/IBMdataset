n, k = map(int,input().split())
s = input()
sakidata = [1]
lastdata = [0]
#data... わける.

mode = False
for cnt, i in enumerate(s):
	if mode:
		if i == "0":
			lastdata.append(cnt)
			mode = False
	else:
		if i == "1":
			sakidata.append(cnt+1)
			mode = True

if mode:
	lastdata.append(cnt+1)

sakidata.append(n)
lastdata.append(n)

ans = 0

#print(sakidata)
#print(lastdata)

for i in range(len(lastdata)-k):
	targ = lastdata[i+k]-sakidata[i]+1
	ans = max(targ, ans)
	
if len(lastdata)-k < 1:
	ans = n

print(ans)