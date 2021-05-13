import sys
input = sys.stdin.readline

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if t * (v - w) >= abs(b - a):
	print("YES")
else:
	print("NO")