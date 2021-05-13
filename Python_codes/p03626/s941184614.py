n = int(input())
s = input()+"?"
i = 0
ref = []
mod = 10**9+7
while i<n:
	if s[i]==s[i+1]:
		ref += [1]
		i += 2
	else:
		ref += [0]
		i += 1
ans = 6 if ref[0] else 3
for i,j in zip(ref,ref[1:]):
	if (1-i)&(1-j):
		ans *= 2
	elif i&(1-j):
		ans *= 1
	elif (1-i)&j:
		ans *= 2
	else:
		ans *= 3
	ans %= mod
print(ans)