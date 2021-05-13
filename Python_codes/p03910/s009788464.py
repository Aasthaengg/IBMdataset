import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def dd(v):
	if v == 1:
		return 1
	ng=1
	ok=v
	while ok - ng>1:
		m=(ok+ng)//2
		if (m*(m+1))//2 >= v:
			#pa('ok',m)
			ok=m
		else:
			#pa('ng',m)
			ng=m
	return ok

def main():
	n = int(input())
	#b , c = IN()
	v=n
	while v > 0:
		r = dd(v)
		print(r)
		v -= r
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)