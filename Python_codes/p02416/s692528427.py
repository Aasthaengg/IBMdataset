while 1:
    s=input();n=0
    if s=="0":
        break
    for i in range(len(s)):
        n+=int(s[i])
    print(n)
