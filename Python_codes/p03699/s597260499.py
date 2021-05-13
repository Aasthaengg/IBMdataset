import sys
n = int(input())
s = [int(input())for S in range(n)]
ans = sum(s)
box = []
if ans%10 != 0:
	print(ans)
	sys.exit()
for i in range(n):
	if (ans-s[i])%10 != 0:
		box.append(ans-s[i])
if len(box) > 0:
	print(max(box))
else:
	print(0)