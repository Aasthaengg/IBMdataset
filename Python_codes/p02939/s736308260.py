s=input()
ans=0
mae=""
now=""
for i in s:
	now += i
	if mae != now:
		ans += 1
		mae = now
		now = ""
print(ans)