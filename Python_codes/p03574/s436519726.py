def CountBomb(box, line, row):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if line+i < 0 or line+i >= len(box) or row+j < 0 or row+j >= len(box[0]):
                continue
            else:
                cell = box[line+i][row+j]
                if cell == "#":
                    count += 1
    return count

def resolve():
    h, w = map(int, input().split())
    box = list()
    for i in range(h):
        a = input()
        b = list()
        for i in range(len(a)):
            b.append(a[i])
        box.append(b)
    
    for line in range(h):
        for row in range(w):
            if box[line][row] == ".":
                box[line][row] = CountBomb(box, line, row)
    
    for line in range(h):
        for row in range(w):
            a = box[line][row]
            print(a, end="")
        print()
resolve()