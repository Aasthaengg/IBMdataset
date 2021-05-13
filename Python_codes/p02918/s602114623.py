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

while(k and cd > 1):

	if cd > 2:
		score += 2 
		cd -= 2
	elif cd == 2:
		score +=1
		cd -= 1
	k -=1
print score