n = int(input().strip())
s = input().strip()
arr = [0] * n
east = 0
west = 0

for i in range(n):
    arr[i] = east
    if s[i] == 'E':
        east += 1
for i in range(n - 1, -1, -1):
    arr[i] += west
    if s[i] == 'W':
        west += 1
ma = max(arr)
idx = i
for i in range(n):
    if arr[i] == ma:
        idx = i
if idx == (n - 1):
    print(s[:idx].count('W'))
else:
    print(s[:idx].count('W') + s[(idx + 1):].count('E'))
