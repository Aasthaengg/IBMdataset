s = input()

for i in range(2**3):
    li = ["+","+","+"]
    for j in range(3):
        if (i >> j) & 1:
            li[j] = "-"
    if eval(s[0] + li[0] + s[1] + li[1] + s[2] + li[2] + s[3]) == 7:
        print(s[0] + li[0] + s[1] + li[1] + s[2] + li[2] + s[3] + "=7")
        exit()