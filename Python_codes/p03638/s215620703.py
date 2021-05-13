h, w = (int(x) for x in input().split())
n = int(input())
seq = [int(x) for x in input().split()]
ans = [[0 for _ in range(w)] for _ in range(h)]
cnt = 0
for color, val in enumerate(seq,1):
    color = str(color)
    for _ in range(val):
        if (cnt // w) % 2 == 0:
            ans[cnt // w][cnt % w] = color
        else:
            ans[cnt // w][-1 - (cnt % w)] = color
        cnt += 1
for line in ans:
    print(' '.join(line))