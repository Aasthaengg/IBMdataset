h,w = map(int, input().split())
s = ["." + str(input()) + "." for i in range(h)]
s.append("."*(w+2))
s.insert(0,"."*(w+2))
l = []

for h in range(1,h+1):
    s1 = ""
    for j in range(1,w+1):
        if s[h][j] == "#":
            s1 += "#"
        else:
            num = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if s[h+x][j+y] == "#":
                        num += 1
            s1 += str((num))
    l.append(s1)
for z in l:
    print(z)