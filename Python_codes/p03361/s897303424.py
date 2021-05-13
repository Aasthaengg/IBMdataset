h, w = list(map(int, input().split()))

s = [list(input()) for _ in range(h)]

flag = True

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            sub_flag = False
            if i > 0 and s[i-1][j] == "#":
                sub_flag = True
            if j > 0 and s[i][j-1] == "#":
                sub_flag = True
            if i < h-1 and s[i+1][j] == "#":
                sub_flag = True
            if j < w-1 and s[i][j+1] == "#":
                sub_flag = True

            if sub_flag:
                pass
            else:
                flag = False
                break

if flag:
    print("Yes")
else:
    print("No")