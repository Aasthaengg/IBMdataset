h, w = map(int, input().split())
Mod = 10**9 + 7
a = [["#"]*(w+1)]
for i in range(h):
    a.append(["#"])
    a[i+1]+=input()
a[1][1] = 1
for i in range(1, h+1):
    for j in range(1, w+1):
        if a[i][j] =="#":
            continue
        elif i==j==1:
            a[i][j] = 1
            continue
        elif a[i-1][j]=="#" and a[i][j-1]=="#":
            a[i][j] = 0
            continue
        elif a[i-1][j] =="#":
            a[i][j] = a[i][j-1]
            continue
        elif a[i][j-1] == "#":
            a[i][j] = a[i-1][j]
            continue
        else:
            a[i][j] = a[i-1][j] + a[i][j-1]
            continue
print(a[h][w]%Mod)