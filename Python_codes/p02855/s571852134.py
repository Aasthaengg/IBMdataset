import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#n = int(input())
	h, w, k = tin()
	#s = input()
	ss = [input() for _ in range(h)]
	ret = [[0]*w for _ in range(h)]
	no_cut = 0
	cut_num = 0
	for hi, hl in enumerate(ss):
		#pa(hl)
		if hl.count('#') == 0 and no_cut >= 0:
			no_cut += 1
			#pa('gggg')
		elif hl.count('#') == 0:
			ret[hi]=ret[hi-1]
			#pa('ghggbh')
		else:
			fs = True
			cut_num += 1
			for wi, c in enumerate(hl):
				if c == '#' and fs:
					fs = False
					ret[hi][wi] = cut_num
				elif c == '#':
					cut_num+=1
					ret[hi][wi]=cut_num
				else:
					ret[hi][wi]=cut_num
			if no_cut >= 0:
				for hii in range(hi):
					ret[hii] = ret[hi]
				no_cut = -1
	for l in ret:
		print(*l)
			
					
				
				
				
			
			
			
	
	
	
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