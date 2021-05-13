s = str(input())
no = 0
while 1:
    for data in ["erase", "eraser", "dream", "dreamer"]:
        if s.endswith(data):
            s = s[: - len(data)]
        else:
            no += 1
    if not s:
        print("YES")
        exit()
    if no == 4:
        print("NO")
        exit()
    else:
        no = 0
