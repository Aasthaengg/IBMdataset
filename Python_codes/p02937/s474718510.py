import collections
s = raw_input()
t = raw_input()
sb = s + s
h = {chr(ord('a') + i):-1 for i in range(26)}
dp = []
for j in range(len(sb)-1,-1,-1):
	dp.append({k:h[k] for k in h})
	h[sb[j]] = j
special = h
dp = dp[::-1]
i = -1
j = 0
c = 0
while(j < len(t)):
	ha = dp[i] if i >= 0 else special
	letter = t[j]
	if ha[letter] != -1:
		i = ha[letter]
		j += 1
	else:
		j = -1
		break

	if i >= len(s):
		i %= len(s)
		c+=1

print (c * len(s) + i + 1) if j != -1 else -1

