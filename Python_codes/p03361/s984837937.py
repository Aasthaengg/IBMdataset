h,w= map(int, input().split())
S = []
t = ["."]*(w+2)
S.append(t)
for i in range(h):
    tmp = ["."]+list(input())+["."]
    S.append(tmp)
S.append(t)

for y in range(1,h+1):
    for x in range(1,w+1):
        if S[y][x] == "#":
            if S[y-1][x] == "." and S[y+1][x] == "." and S[y][x+1] == "." and S[y][x-1] == ".":
                print("No")
                exit()
print("Yes")