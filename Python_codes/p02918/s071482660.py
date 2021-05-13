n, k = [int(i) for i in input().split()]
s = input()
n_group = 0
now = s[0]
cnt = 0
happy = 0
s += 'z'
for i in s:
	if now != i:
		n_group += 1
		if cnt > 1:
			happy += cnt - 1
		cnt = 1
	else:
		cnt += 1
	now = i

for i in range(k):
	if n_group > 2:
		n_group -= 2
		happy += 2
	else:
		happy += 1
if happy > n - 1:
	happy = n - 1
print (happy)