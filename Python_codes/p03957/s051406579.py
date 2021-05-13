import sys
input = sys.stdin.readline

# A - CF
s = input()
n = s.find('C')

if n > -1:
	if 'F' in s[n:]:
		print('Yes')
		exit()

print('No')