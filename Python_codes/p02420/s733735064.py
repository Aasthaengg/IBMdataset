while 1:
    s = input()
    if s == '-':
        break
    else:
        N = int(input())
        for n in range(N):
            h = int(input())
            s = s[h:]  + s[0 : h]
        print(s)
