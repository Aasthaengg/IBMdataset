s = raw_input()
q = int(raw_input())
for i in range(q):
	m = raw_input().split(' ')
	if m[0]=="print":
		print s[int(m[1]):int(m[2])+1]
	elif m[0] == "replace":
		s = s[:int(m[1])]+m[3]+s[int(m[2])+1:]
	else:
		t = s[int(m[1]):int(m[2])+1]
		s = s[:int(m[1])]+t[::-1]+s[int(m[2])+1:]