S = input()

now = "aa"
tmp = ""
ans = 0

for s in S:
	tmp += s
	if tmp != now:
		ans += 1
		now = tmp
		tmp = ""	

print(ans)	
