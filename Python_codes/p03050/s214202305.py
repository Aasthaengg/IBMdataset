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
	return maa(n)
	#b , c = tin()
	#s = input()
	for i in range(1,10000):
		if maa(i)!=mab(i):
			pa(maa(i), mab(i))
			return i
	print('ok')
	
def maa(n):
	ret = 0
	rr=[]
	for i in range(1, n+1):
		if n//i <= i:
			break
			
		if (n-i) % i == 0:
			if i == (n-i)//i:
				return ret
			#pa(i, (n-i)//i)
			ret += (n-i)//i
			#rr.append((n-i)//i)
			
	return ret
	
def mab(n):
	ret = 0
	for i in range(1, n+1):
		if n // i == n%i:
			ret += i
	return ret
	
	
#+++++
isTest=False

def pa(*vl):
	if not isTest:
		return
	print(*vl)
		
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