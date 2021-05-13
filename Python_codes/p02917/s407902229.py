
n = int(raw_input())
b = map(int, raw_input().split(' '))
def f(b):
	n = len(b)+1
	s = 0
	for i in range(n):  s += min(b[i] if i < n-1 else +float('inf'), b[i-1] if i-1>=0 else +float('inf'))
	return s
print f(b)
