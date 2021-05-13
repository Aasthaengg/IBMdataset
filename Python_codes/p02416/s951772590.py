while True:
    s = input()
    if s == "0":
        break
    a = 0
    for i,j in enumerate(s):
        a += int(s[i])
    print(a)
