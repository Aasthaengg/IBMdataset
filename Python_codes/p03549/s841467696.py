import sys
sys.setrecursionlimit(10**6)
if sys.platform in (['ios','darwin','win32']):
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]
LONG = 1900
SHORT = 100
N, M = MAP()

sh = (N-M)*SHORT
lo = M*LONG
prob = 2**M
#print(sh, lo, prob)
print((sh+lo)*prob)