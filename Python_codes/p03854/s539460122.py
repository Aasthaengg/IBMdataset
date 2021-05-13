words = ['dream','dreamer', 'erase', 'eraser']
s = raw_input()
dp = [False for _ in range(len(s))]

for j in range(len(s)):
	for w in words:
		b = dp[j - len(w)] if j - len(w) -1 >= 0 else True
		b &= j-len(w) +1 >= 0 and s[j- len(w)+1:j+1] == w
		if b:
			dp[j] = True
			break
print 'YES' if dp[-1] else 'NO'