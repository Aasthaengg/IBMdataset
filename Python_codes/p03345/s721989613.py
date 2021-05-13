import sys
sys.setrecursionlimit(10**6)
if sys.platform in (['ios','darwin','win32']):
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

def main():
	A, B, C, K = MAP()
	dif = A-B
	if dif > 10**18:
		print('Unfair')
	elif K%2:
		print(-dif)
	else:
		print(dif)

if __name__ == '__main__':
	main()