from sys import stdin
input = stdin.buffer.readline

n = int(input())
*a, = map(int, input().split())
b = 1000
for i in range(n - 1):
	if a[i] < a[i + 1]:
		b = b // a[i] * a[i + 1] + b % a[i]
print(b)
