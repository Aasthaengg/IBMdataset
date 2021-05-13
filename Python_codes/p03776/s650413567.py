import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def conv(bb, n):
	ret = 1
	for i in range(bb-n+1, bb+1):
		ret *= i
	for i in range(1, n+1):
		ret //= i
	return ret

def main():
	#a = int(input())
	n, a, b = tin()
	#s = input()
	al = lin()
	al.sort(reverse=True)
	bb = sum(al[:a])/a
	print(bb)
	
	min_use = al[a]
	rrc = al.count(min_use)
	if al[0] == min_use:
		ret = 0
		for n in range(a, min(b, rrc)+1):
			ret += conv(rrc, n)
		print(ret)
		return 
	else:
		rr = [v for v in al if v >= min_use]
		zettai=len(rr)-rrc
		nokori = a- zettai
		n_pattern = conv(rrc, nokori)
		print(n_pattern)
		return
	
	
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