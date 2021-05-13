import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = tin()
	#s = input()
	al = lin()
	flg=None
	dd = 1
	pv=al[0]
	for v in al[1:]:
		if flg is None:
			if pv == v:
				pass
			elif pv < v:
				flg = 'up'
			else:
				flg = 'down'
		elif flg == 'up':
			if v < pv:
				dd += 1
				flg = None
		else:
			if v > pv:
				dd += 1
				flg = None
		pv = v
	print(dd)
				
	
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