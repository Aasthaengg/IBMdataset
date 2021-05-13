import sys
n, m, x, y = map(int, input().split())
x1 = max(list(map(int, input().split())))
y1 = min(list(map(int, input().split())))


for i in range(x+1, y+1):
    if x1 < i <= y1:
        print('No War')
        sys.exit()
print('War')

