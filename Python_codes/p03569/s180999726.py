import sys

s = sys.stdin.readline().strip()

ans = 0
l = 0
r = len(s) - 1

while l < r:
    # print("left", l, "right", r)
    if s[l] == "x" and s[r] == "x":
        l += 1
        r -= 1
    # rにxを足したとみなし、lを進める
    elif s[l] == "x":
        l += 1
        ans += 1
    # lにxを足したとみなし、rを進める
    elif s[r] == "x":
        r -= 1
        ans += 1
    elif s[l] != s[r]:
        print(-1)
        sys.exit()
    else:
        l += 1
        r -= 1

print(ans)