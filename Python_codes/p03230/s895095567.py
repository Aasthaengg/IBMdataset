import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def gg(n):
	for i in range(n+1):
		#print(2*n, i*i+1)
		if 2*n == i*(i+1):
			return i+1
		if 2*n < i*(i+1):
			return -1
	return -1

def main():
	n = int(input())
	#b , c = tin()
	#s = input()
	g_num = gg(n)
	if g_num == -1:
		return 'No'
	print('Yes')
	print(g_num)
	n_num = g_num-1
	ggg=[]
	ggg.append(list(range(1, n_num+1)))
	next=n_num+1
	for ig in range(g_num-1):
		next_group=[]
		for ip, g in enumerate(ggg):
			next_group.append(g[len(ggg)-1])
		while len(next_group) < n_num:
			next_group.append(next)
			next+=1
		ggg.append(next_group)
	for g in ggg:
		print(n_num, *g)
	
		
	
	
	
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