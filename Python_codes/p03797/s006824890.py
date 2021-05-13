import sys
if sys.platform in ['ios', 'win32', 'darwin']:
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(x) for x in input().split()]

S, C = MAP()

ans = 0

tmp = min(S//1, C//2)
ans += tmp
S -= tmp*1
C -= tmp*2

if C >=4: ans += C//4

print(ans)