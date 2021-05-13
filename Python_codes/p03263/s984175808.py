

def submit():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    stroke = []
    direction = 1
    for i in range(w):
        if direction == 1:
            st, ed = 0, h
        else:
            st, ed = h - 1, -1
        for j in range(st, ed, direction):
            stroke.append((j, i))
        st, ed = ed, st
        direction *= -1

    moves = []
    cnt = 0
    for s, e in zip(stroke, stroke[1:]):
        if a[s[0]][s[1]] % 2:
            cnt += 1
            moves.append((s, e))
            a[e[0]][e[1]] += 1
    
    print(cnt)
    for s, e in moves:
        print("{} {} {} {}".format(s[0] + 1, s[1] + 1, e[0] + 1, e[1] + 1))


submit()