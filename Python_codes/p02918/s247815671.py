n,k = map(int, raw_input().split())
s = raw_input()
cd = 0
d = None
for l in s:
	if d != l:
		cd +=1
		d = l
score = 0
for u,v in zip(s,s[1:]):
	if u == v:
		score +=1

if cd > 2:
	t = min(k,((cd - 2)+1)/2)
	k -= t
	score += 2 * t 
	cd -= 2 * t
if cd == 2 and k:
	score +=1
	cd -= 1
print score