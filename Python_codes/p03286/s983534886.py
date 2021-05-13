n = int(input())
def encode(k):
	if k==0:
		return '0'
	if k==1:
		return '1'
	if k % 2 == 0:
		string = '{}0'.format(encode(k // (-2)))
		return string
	if k % 2 == 1:
		string = '{}1'.format(encode((k-1) // (-2)))
		return string

print(encode(n))