import sys
read = sys.stdin.buffer.read
readline = sys.stdin.readline
readlines = sys.stdin.buffer.readlines

S = readline().rstrip()
S = S.replace('BC', '#')

tmp = 0
ans = 0
for i in range(len(S)-1,-1,-1):
	if S[i] == "#":
		tmp += 1
	elif S[i] == "A":
		ans += tmp
	else:
		tmp = 0
print(ans)
