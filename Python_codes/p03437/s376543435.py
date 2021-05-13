import sys

use_clipboard=True

def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if sys.platform =='ios':
	if use_clipboard:
		ic=input_clipboard()
		input = lambda : ic.__next__()
	else:
		sys.stdin=open('inputFile.txt')


	
#+++++

x, y = map(int, input().split())
ret = x if x % y != 0 else -1
print(ret)