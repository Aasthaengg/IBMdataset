# B - KEYENCE String
def is_keyence_string():
	for i in range(1, len(key)):
		left = key[:i]
		right = key[i-len(key):]
		
		if S.startswith(left) and S.endswith(right):
			return True
	
	return False


S = input().strip()
key = 'keyence'

if S.startswith(key):
	print('YES')
elif S.endswith(key):
	print('YES')
elif is_keyence_string():
	print('YES')
else:
	print('NO')