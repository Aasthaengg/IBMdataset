s = input()
ans = 10000
for i in range(len(s)-2):
	num = int(s[i] + s[i+1] + s[i+2])
	if abs(num-753) < ans:
		ans = abs(num-753)
print(ans)
