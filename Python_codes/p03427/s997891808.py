n = int(input())

def get_first(n):
	return int(str(n)[0])

def check(n):
	# x99..99かどうか
	s = str(n)
	for i in range(1, len(str(n))):
		if str(s[i]) != '9':
			return False
	return True

if check(n):
	res = get_first(n) + 9 * (len(str(n)) - 1)
else:
	res = (get_first(n) - 1) + 9 * (len(str(n)) - 1)

print(res)