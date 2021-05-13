n = int(input())

ans = []

while (n != 0):
	r = n % 2
	if r < 0:
		r += 2

	n = (n - r) // (-2)
	ans.append(r)

if ans == []:
	ans.append(0)
ans = ans[::-1]

print(*ans, sep='')