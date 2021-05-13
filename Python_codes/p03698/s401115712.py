import collections

S = input()

l = collections.Counter(S).values()
if(max(l)>1):
	print('no')
else:
	print('yes')