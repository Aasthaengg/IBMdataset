n, p = [int(i) for i in input().split()]
s = input()




digit_rm = [0 for _ in range(n)]
for i in range(n):
	digit_rm[i] = (int(s[n-1-i]) * pow(10, i, p) ) % p

remain = [0 for _ in range(n)]
for i in range(n):
	if i == 0:
		remain[i] = digit_rm[i]
	else:
		remain[i] = (remain[i-1] + digit_rm[i]) % p

pcnt = [0 for _ in range(p)]

for i in remain:
	pcnt[i] += 1

if 10 % p == 0:
	ans = 0
	for i in range(n):
		if int(s[n-1-i]) % p == 0:
			ans += n - i
	print(ans)
else:
	ans = pcnt[0]
	for num in pcnt:
		if num != 0:
			ans += num * (num - 1) // 2

	print(ans)





