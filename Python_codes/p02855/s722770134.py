from sys import stdin

h,w,k = [int(x) for x in stdin.readline().rstrip().split()]
li = [["" for i in range(w)]for j in range(h)]
for i in range(h):
    s = stdin.readline().rstrip()
    for j in range(w):
        li[i][j] = s[j]
lin = [[0 for i in range(w)]for j in range(h)]
count = 0
for i in li:
    if "#" not in i:
        count += 1
    else:
        break
point = 0
for i in range(count,h):
    kosuu = li[i].count("#")
    if kosuu == 0:
        for j in range(w):
            lin[i][j] = lin[i-1][j]
    else:
        point += 1
        kai = 0
        for k in range(w):
            lin[i][k] = point
            if li[i][k] == "#":
                kai += 1
                if kai < kosuu:
                    point += 1
for i in range(count):
    for j in range(w):
        lin[i][j] = lin[count][j]
for i in lin:
    print(*i)