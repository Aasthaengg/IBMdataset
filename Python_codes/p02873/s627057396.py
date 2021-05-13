s = input()
l = len(s)

a1 = [0]*(l+1)
a2 = [0]*(l+1)

for i in range(l):
	if s[i] == "<":
		a1[i+1] = a1[i] + 1
	else:
		a1[i+1] = 0

for i in range(l):
	if s[-i-1] == ">":
		a2[i+1] = a2[i] + 1
	else:
		a2[i+1] = 0

cnt = 0
for i in range(l+1):
	cnt += max(a1[i],a2[-i-1])

print(cnt)