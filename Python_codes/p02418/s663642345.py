s = raw_input()
s_2 = ''
judge = 0
p = raw_input()
for i in range(len(s)):
	s_list = list(s)
	if list(s)[i] == list(p)[0]:
		s_list.extend(s_list[0:i])
		del s_list[0:i]
		s_2 = "".join(s_list)
		if p in s_2:
			judge = 1
if judge :
	print 'Yes'
else :
	print 'No'