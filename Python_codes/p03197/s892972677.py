import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

'''
奇数の果実が有れば先行の勝ち。
初手で全ての果実の個数が偶数になるようにとれば、
あとは、後攻の真似をし続けることができる。

一方、全ての果実が偶数なら、後攻は先攻の真似をすれば良い。

'''

def main():
	n = int(input())
	#b , c = tin()
	#s = input()	
	for i in range(n):
		v = int(input())
		if v % 2 == 1:
			return 'first'
	return 'second'
	
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