h, w = map(int, input().split())
l = []
for i in range(h):
    l.append(list(input()))
for i in range(h):
    for j in range(w):
        num_mine = 0
        if l[i][j] != "#":
            if 0<i and 0<j and l[i-1][j-1] == "#":
                num_mine += 1
            if 0<i and l[i-1][j] == "#":
                num_mine += 1
            if 0<i and j<w-1 and l[i-1][j+1] == "#":
                num_mine += 1
            if 0<j and l[i][j-1] == "#":
                num_mine += 1
            if j<w-1 and l[i][j+1] == "#":
                num_mine += 1
            if i<h-1 and 0<j and l[i+1][j-1]== "#":
                num_mine += 1
            if i<h-1 and l[i+1][j] == "#":
                num_mine += 1
            if i<h-1 and j<w-1 and l[i+1][j+1] == "#":
                num_mine += 1
            l[i][j] = str(num_mine) 
for i in range(h):
    print(''.join(l[i]))           