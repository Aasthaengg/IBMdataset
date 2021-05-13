import math
s=input()
n=len(s)
flist=[0]*n

rstreak=False
tmpl=0
tmpr=0
divindex=0

for i in range(n):
	if rstreak:
		if s[i] == "R":
			tmpr += 1
		else:
			rstreak = False
			divindex = i-1
			tmpl += 1
	else:
		if s[i] == "R":
			rstreak=True
			flist[divindex]=math.ceil(tmpr/2) + tmpl//2
			flist[divindex+1]=math.ceil(tmpl/2) + tmpr//2
			tmpl=0
			tmpr=1
		else:
			tmpl += 1

flist[divindex]=math.ceil(tmpr/2) + tmpl//2
flist[divindex+1]=math.ceil(tmpl/2) + tmpr//2

for f in flist:
	print(f,end=" ")
