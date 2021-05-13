s = input()
now = len(s)
while 1:
    flag = 1
    if 7 <= now:
        if s[now-7:now] == "dreamer":
            now -= 7
            flag = 0
    if 6 <= now:
        if s[now-6:now] == "eraser":
            now -= 6
            flag = 0
    if 5 <= now:    
        if s[now-5:now] == "erase":
            now -= 5
            flag = 0
        if s[now-5:now] == "dream":
            now -= 5
            flag = 0
    if flag:
        print("NO")
        exit()
    if now == 0:
        print("YES")
        exit()
    elif now < 5:
        print("NO")
        exit()