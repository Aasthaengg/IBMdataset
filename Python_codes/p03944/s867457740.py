def coloring():
    line = input()
    words = line.split()
    W = int(words[0])
    H = int(words[1])
    N = int(words[2])

    x = 0
    y = 0
    w = W
    h = H

    grid = []

    for i in range(h):
        for j in range(w):
            grid.append(0)

    for i in range(N):
        s = input()
        ws = s.split()
        x = int(ws[0])
        y = int(ws[1])
        a = int(ws[2])
        if a == 1:
            #rect = x * whole
            for i in range(h):
                for j in range(x):
                    grid[j + w * i] = 1

        if a == 2:
            #rect = (w - x) * whole
            for i in range(h):
                for j in range(x,w):
                    grid[j + w*i] = 1

        if a==3:
            #rect = whole * y
            for i in range(y):
                for j in range(w):
                    grid[j + w * i] = 1
        
        if a == 4:
            #rect = whole * (h - y)
            for i in range(y,h):
                for j in range(w):
                    grid[j + w*i] = 1

        
    print(grid.count(0))


coloring()