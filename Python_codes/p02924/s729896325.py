import sys
sys.setrecursionlimit(10**6)
if sys.platform in (['ios','darwin','win32']):
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

def main():
	N = INT()
	M = N-1
	ans = (1+M)*M//2
	print(ans)

if __name__ == '__main__':
	main()