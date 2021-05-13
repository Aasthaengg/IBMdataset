# A - Diverse Word
def is_various(s):
	if len(s) == len(set(s)):
		return True


import string
lower = string.ascii_lowercase

S = input()

for c in lower:
	next = S + c
	
	if  len(set(next)) == len(S) + 1:
		print(next)
		exit()

for i in range(1, len(S) + 1):
	left = S[:len(S)-i]
	right = S[-i:]
	
	start = right[0]
	is_start = False

	for c in lower:
		if is_start:
			next = left + c
			
			if is_various(next):
				print(next)
				exit()
		
		if c == start:
			is_start = True
		
print(-1)