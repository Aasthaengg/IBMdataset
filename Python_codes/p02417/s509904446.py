import sys

cnt = [0 for i in xrange(26)]

for e_string in sys.stdin:

	for i in e_string:
		j = ord(i)
		if   j >= 65 and j <= 90:
			cnt[j%65] += 1
		elif j >= 97 and j <= 122:
			cnt[j%97] += 1
		else:
			continue

for i in xrange(26):
	print u"%c : %d" % (chr(97+i), cnt[i])