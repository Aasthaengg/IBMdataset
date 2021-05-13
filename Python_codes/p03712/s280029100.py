H,W = map(int, input().split())
a = [0 for _ in range(H)]

for i in range(H):
	a[i] = '#'+input()+'#'
    
for i in range(H+2):
	if i == 0 or i == H+1:
		print('#'*(W+2))
	else:
		print(a[i-1])