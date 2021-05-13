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
	dd = dict()
	
	v = int(input())
	dd[v] = 0
	ll=[0]*n
	ll[0]=1
	for i in range(1, n):
		v = int(input())
		if v not in dd or dd[v] == i-1:
			ll[i] = ll[i-1]
			dd[v] = i
		else:
			ll[i] = (ll[i-1] + ll[dd[v]])%mod
			dd[v] = i
	return ll[-1]
			
		
	
	
	
	
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