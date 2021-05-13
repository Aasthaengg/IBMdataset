H, W = list(map(int,input().split()))
s = []
for i in range(H):  s.append(input())
def solve():
    for i in range(H):
        for j in range(W):
            if s[i][j] == "#":
                flg = 1
                if i >= 1:
                    if s[i - 1][j] == "#":
                        flg = 0
                if i < H - 1:
                    if s[i + 1][j] == "#":
                        flg = 0
                if j >= 1:
                    if s[i][j - 1] == "#":
                        flg = 0
                if j < W - 1:
                    if s[i][j + 1] == "#":
                        flg = 0
                if flg:  return "No"
    return "Yes"
ans = solve()
print(ans)