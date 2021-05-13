H, W = map(int, input().split())

s = [["."] * (W + 2) for i in range(H+2)]

for i in range(1, H + 1):
    ss = input()
    for j in range(1, W + 1):
        s[i][j] = ss[j-1]

#print(s)
f = 0

for i in range(1, H+1):
    for j in range(1, W+1):
        if s[i][j] == "#" and s[i+1][j] == "." and s[i-1][j] == "." and s[i][j+1] == "." and s[i][j-1] == ".":
            f =1
    if f == 1:
        break

if f == 0:
    print("Yes")
else:
    print("No")
