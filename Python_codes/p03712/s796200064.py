h, w = map(int, input().split())
tb = ['#'] * (w + 2)
print(*tb, sep='')
for i in range(h):
	print('#' + input() + '#')
print(*tb, sep='')