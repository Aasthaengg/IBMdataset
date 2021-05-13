import itertools
h, w = map(int,input().split())
masu = []
for _ in range(h):
    masu.append(list(input()))

for i in range(h):
    for j in range(w):
        if masu[i][j] == '.':
            continue

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for d in directions:
            if 0 <= i + d[0] <= h-1 and 0 <= j + d[1] <= w-1:
                if masu[i+d[0]][j+d[1]] != '.':
                    masu[i][j] = '黒'
                    masu[i + d[0]][j + d[1]] = '黒'

if '#' in list(itertools.chain.from_iterable(masu)):
    print('No')
else:
    print('Yes')