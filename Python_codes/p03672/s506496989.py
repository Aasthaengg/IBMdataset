s = input()

end = len(s) - 1
half = int(len(s) / 2) - 1
flag = True
while end != 1:
    end -= 2
    half -= 1
    start = 0
    flag = True
    for i in range(half+1, end):
        if s[i] != s[start]:
            flag = False
            break
        start += 1
    if flag == True:
        print(end+1)
        exit()


