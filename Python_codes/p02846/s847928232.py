import sys

#+++++
		
def main():
	t1, t2 = map(int, input().split())
	a1, a2 = map(int, input().split())
	b1, b2 = map(int, input().split())
	
	a_d = t1*a1 + t2 * a2
	b_d = t1*b1 + t2 * b2
	
	if a_d == b_d:
		return 'infinity'
	
	pp=a_d-b_d
	pc=t1*(a1-b1)
	if pp*pc > 0:
		return 0
	
	#pa((pp,pc))

		
	return (2 * (-pc // pp) + 1) -(1 if pc % pp == 0 else 0)
	
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