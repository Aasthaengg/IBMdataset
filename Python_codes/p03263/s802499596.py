import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def ggg(h,w):
	a=0
	b=0
	while b < h:
		if b%2==0 and a == w-1:
			na = a
			nb = b+1
		elif b %2==0:
				na = a+1
				nb = b
		elif a == 0:
			na=a
			nb = b+1
		else:
			na = a-1
			nb = b
		yield a, b, na, nb
		a=na
		b=nb


def main():
	#a = int(input())
	h, w = tin()
	#s = input()
	mp = [lin() for _ in range(h)]
	ret = []
	lg = ggg(h, w)
	oddf = False
	for a, b, na, nb in lg:
		if mp[b][a] %2 == 1:
			oddf = not oddf
		if oddf and nb < h:
			ret.append([b+1, a+1, nb+1,na+1])
	print(len(ret))
	for k in ret:
		print(*k)
	
	
	
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