import sys

n = int(input())
h = list(map(int, input().split(' ')))
max = 0
for i in range(len(h)):
    if max < h[i]:
        max = h[i]
    if h[i]+2 <= max:
        print('No')
        sys.exit()
print('Yes')
