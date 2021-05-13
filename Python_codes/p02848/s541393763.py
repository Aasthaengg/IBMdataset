N = int(input())
S = input()
ans = ''
for s in S:
	ans += chr(ord(s) + N) if ord(s) < (ord('Z') - N + 1) else chr(ord(s) - 26 + N)
print(ans)
