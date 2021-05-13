h, w = map(int, input().split())
A = []
for _ in range(h):
	A.append(input())
B = ['#'] * (w + 2)
print(''.join(B))
for e in A:
	print('#' + e + '#')
print(''.join(B))
