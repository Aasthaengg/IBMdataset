H, W = map(int, input().split())
s = []
s.append(["."]*(W+2))
for _ in range(H):
    string = input()
    string = "." + string + "."
    s.append(list(string))
s.append(["."]*(W+2))
ans = True
for row in range(1, H+1):
    for col in range(1, W+1):
        if s[row][col] == "#":
            is_ok = False
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if s[row+dh][col+dw] == "#":
                    is_ok = True
                    break
            if not is_ok:
                ans = False
                break
if ans:
    print("Yes")
else:
    print("No")