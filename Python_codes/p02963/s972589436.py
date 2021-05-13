import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def cc(s):
	if s <= 10**9:
		r = [0,0,s,0,0,1]
		return r
		
	ok=10**9
	ng=1
	while ok-ng > 1:
		mid = (ok+ng)//2
		if mid * mid >= s:
			ok = mid
		else:
			ng = mid
	if ok*ok == s:
		r = [0,0,ok,0,0,ok]
		return r
		
	mx = ok
	ok = mx
	ng = 1
	while ok - ng > 1:
		mid = (ok+ng)//2
		if mx * mid >= s:
			ok = mid
		else:
			ng = mid
			
	if mx * ok == s:
		return [0,0,mx, 0, 0, ok]
		
	else:
		diff = (mx * ok) - s
		#dd=s-(mx*ok)
		#pa(dd)
		#pa(mx*ok-diff)
		#pa(s)
		return [0,0,mx,1,diff, ok]
		
	
	
		
		

def main():
	s = int(input())
	#b , c = tin()
	#s = input()
	ret = cc(s)
	print(*ret)
		
		
	
	
	
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