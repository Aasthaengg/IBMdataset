n = int(input())
a = list(map(int, input().split()))
cnt1 = 0
s = 0
swc = 1
for i in a:
	s += i
	if swc == 1:
		swc = 0
		if s > 0:
			continue
		else:
			cnt1 += 1-s
			s = 1
	else:
		swc = 1
		if s < 0:
			continue
		else:
			cnt1 += s+1
			s = -1
swc = 0
cnt2 = 0
s= 0
for i in a:
	s += i
	if swc == 1:
		swc = 0
		if s > 0:
			continue
		else:
			cnt2 += 1-s
			s = 1
	else:
		swc = 1
		if s < 0:
			continue
		else:
			cnt2 += s+1
			s = -1
print (min(cnt1, cnt2))
