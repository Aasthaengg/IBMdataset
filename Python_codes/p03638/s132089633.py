

def submit():
    h, w = map(int, input().split())
    n = int(input())
    alist = list(map(int, input().split()))

    color = [[0 for _ in range(w)] for _ in range(h)]
    cur = 1

    # 一筆書きする
    direction = 1
    for i in range(h):
        if direction == 1:
            j = 0
        else:
            j = w - 1

        while 0 <= j < w:
            if alist[cur - 1] <= 0:
                cur += 1          
            color[i][j] = cur
            alist[cur - 1] -= 1
            j += direction

        direction *= -1
                

    for c in color:
        print(" ".join(map(str, c)))


submit()