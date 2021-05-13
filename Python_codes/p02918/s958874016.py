n,k = map(int, raw_input().split())
score,d,cd = 0,None,0
s = raw_input()
for i,l in enumerate(s):
	if d != l:
		cd +=1
		d = l
	if i and s[i-1] == s[i]:  score += 1


if cd > 2:
	t = min(k,((cd - 2)+1)/2)
	k -= t
	score += 2 * t 
	cd -= 2 * t
if cd == 2 and k:
	score +=1
	cd -= 1
print score
