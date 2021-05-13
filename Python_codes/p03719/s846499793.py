import sys
bbn=1000000007
	
#+++++
		
def main():
	a, b , c = map(int, input().split())
	ret = 'Yes' if (a <= c and c <= b) else 'No'
	print(ret)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)