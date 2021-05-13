h, w = map(int, input().split())

lis = []
tmp =["."]*(w+2)
lis.append(tmp)

for i in range(h):
    a = ["."]+list(input())+["."]
    lis.append(a)

lis.append(tmp)

for i in range(1,h+1):
    for j in range(1,w+1):
        if lis[i][j] == "#":
            continue
        
        else:
            n = 0
            if lis[i-1][j-1] == "#":
                n += 1
            if lis[i-1][j] == "#":
                n += 1
            if lis[i][j-1] == "#":
                n += 1
            if lis[i][j+1] == "#":
                n += 1
            if lis[i+1][j-1] == "#":
                n += 1
            if lis[i+1][j] == "#":
                n += 1
            if lis[i+1][j+1] == "#":
                n += 1
            if lis[i-1][j+1] == "#":
                n += 1
            
            lis[i][j] = n

for i in range(1, h+1):
    for j in range(1, w+1):
        print(lis[i][j], end="")
    print()
   