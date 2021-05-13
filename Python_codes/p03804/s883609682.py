import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def tm(a, b, hi, wi):
	lb=len(b[0])
	for i, bi in enumerate(b):
		if a[hi+i][wi: wi+lb] != bi:
			return False
	return True
	


def main():
	#a = int(input())
	n, m = tin()
	#s = input()
	al=[input() for _ in range(n)]
	bl=[input() for _ in range(m)]
	for hi in range(n-m+1):
		for wi in range(n-m+1):
			if tm(al, bl, hi, wi):
				return 'Yes'
	return 'No'
	
	
	
	
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