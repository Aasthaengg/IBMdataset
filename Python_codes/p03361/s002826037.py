[h,w] = [int(i) for i in input().split()]
ls = [["."] * (w+2)]
for i in range(h):
    tmp = input()
    tmp_ls = ["."]
    for j in range(w):
        tmp_ls.append(tmp[j])
    tmp_ls.append(".")
    ls.append(tmp_ls)
ls.append(["."] * (w+2))
ans = "Yes"

for i in range(1,h+1):
    for j in range(1,w+1):
        flag = 0
        if ls[i][j] == "#":
            flag = flag or (ls[i-1][j] == "#")
            flag = flag or (ls[i+1][j] == "#")
            flag = flag or (ls[i][j-1] == "#")
            flag = flag or (ls[i][j+1] == "#")
            if flag == 0:
                ans = "No"
print(ans)
