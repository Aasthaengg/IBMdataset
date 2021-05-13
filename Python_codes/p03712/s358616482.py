H,W = map(int, input().split())

a = list()
for i in range(H):
	a.append(input())

for _ in range(W+2): print('#', end='')
print()

for i in range(H):
	print('#', end='')
	print(a[i], end='')
	print('#')
	
for _ in range(W+2): print('#', end='')
print()