import sys

s = input()
if s == "zyxwvutsrqponmlkjihgfedcba":
	print(-1)
	sys.exit()
if len(s) < 26:
	flg = [0] * 26
	for i in range(len(s)):
		flg[ord(s[i])-97] = 1
	ans = s + chr(flg.index(0)+97)
	print(ans)

else:
	candidate = []
	for i in range(25,0,-1):
		candidate.append(s[i])
		if s[i-1] < s[i]:
			obj = s[i-1]
			ind = i-1
			break

	candidate.append(obj)
	candidate.sort()
	switch = candidate[candidate.index(obj)+1]
	ans = s[:ind] + switch
	print(ans)