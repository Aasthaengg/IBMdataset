import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
	a,b = map(int,input().split())
	idx = b - a
	ans = 0
	for i in range(idx):
		ans += i
	ans -= a
	print(ans)
	

if __name__ == '__main__':
	main()