string = input()
r = []
for index, s in enumerate(string):
	if (index + 1 ) % 2 != 0:
  		r.append(s)
print(''.join(r))