def change(w,b):
    h = 0
    grid = []
    for i in range(50):
        if i % 3 == 0:
            grid.append([1 for j in range(100)])
        elif i % 3 == 1:
            grid.append([])
            for j in range(100):
                if w > 1 and j % 2 and j < 99:
                    grid[i].append(0)
                    w -= 1
                else:
                    # print(i)
                    grid[i].append(1)
        elif i % 3 == 2:
            grid.append([])
            for j in range(100):
                if w > 1 and j % 2 == 0 and j < 99:
                    grid[i].append(0)
                    w -= 1
                else:
                    grid[i].append(1) 
    b -= 1
    for i in range(50, 100):
        if i % 3 == 2:
            grid.append([0 for j in range(100)])
        elif i % 3 == 0:
            grid.append([])
            for j in range(100):
                if b > 0 and j % 2 and j < 99:
                    grid[i].append(1)
                    b -= 1
                else:
                    grid[i].append(0) 
        elif i % 3 == 1:
            grid.append([])
            for j in range(100):
                if b > 0 and j % 2 == 0 and j < 99:
                    grid[i].append(1)
                    b -= 1
                else:
                    grid[i].append(0) 

    print(100,100)
    d = {0:'.', 1:'#'}    
    [print(''.join(map(d.get,line))) for i,line in enumerate(grid)]

w,b = map(int, input().split())
# w=0, b=1
change(w,b)
