s = input()
n = len(s)
idx = n
while idx > 0:
    flag = 0
    if idx >= 7:
        if s[idx - 7 : idx] == "dreamer":
            idx -= 7
            flag = 1
    if idx >= 6:
        if s[idx - 6 : idx] == "eraser":
            idx -= 6
            flag = 1
    if idx >= 5:
        if s[idx - 5 : idx] == "dream" or s[idx - 5 : idx] == "erase":
            idx -= 5
            flag = 1
    if idx < 5:
        break
    if not flag:
        break
if not idx:
    print("YES")
else:
    print("NO")

