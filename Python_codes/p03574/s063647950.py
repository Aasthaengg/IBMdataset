h, w = map(int, input().split())
s = [input() for _ in range(h)]

for i in range(h):
    result = []
    for j in range(w):
        if s[i][j] == '#':
            result.append('#')
        elif s[i][j] == '.':
            cnt = 0
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if 0 <= i+y <= h-1:
                        if 0 <= j+z <= w-1:
                            if s[i+y][j+z] == '#':
                                cnt += 1
            result.append(str(cnt))
    print(*result, sep='')

