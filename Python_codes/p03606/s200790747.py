s = 0
for _ in range(int(raw_input())):
	l,r = map(int, raw_input().split())
	s += r - l +1
print s
