s = list(input())
n = len(s) + 1

i = 0
left = 0
right = 0
ans = 0
tmp = 0

while i < n-1:
	if s[i] == '<':
		break
	i += 1
	tmp += 1
ans += tmp * (tmp + 1) // 2
while i < n-1:
	if i == n-2:
		if s[i] == '>':
			right += 1
			break
		else:
			left += 1
			break
	if s[i] == '<' and s[i+1] == '>':
		left += 1
		while True:
			if s[i+1+right] == '>':
				right += 1
				if i+1+right == n-1:
					break
			else:
				break
		if left >= right:
			ans += left * (left + 1) // 2 + (right - 1) * right // 2
		else:
			ans += right * (right + 1) // 2 + (left - 1) * left // 2
		i += right + 1
		left = 0
		right = 0
	elif s[i] == '<':
		left += 1
		i += 1

print(ans + left * (left + 1) // 2 + right * (right + 1) // 2 )
