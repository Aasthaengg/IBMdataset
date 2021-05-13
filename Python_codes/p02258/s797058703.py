s_max = -float('inf')
s = 0
for i in range(int(input())):
	r = int(input())
	if i:
		d = r - prev
		s = max(s, 0) + d
		s_max = max(s, s_max)
	prev = r
print(s_max)
