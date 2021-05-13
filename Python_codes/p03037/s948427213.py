n, m = map(int, input().split())
 
max_left = 1
min_right = n
 
for i in range(m):
    left, right = map(int, input().split())
    max_left = max(max_left, left)
    min_right = min(min_right, right)
 
print(max(min_right - max_left + 1, 0))