s = input()

a = list('abcdefghijklmnopqrstuvwxyz')

if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
elif len(s) < 26:
    for x in a:
        if s.count(x) == 0:
            print(s + x)
            break
else:
    end = False
    for i in range(25)[::-1]:
        if end:
            break
        for j in range(i+1,26)[::-1]:
            if s[i] < s[j]:
                print(s[:i]+s[j])
                end = True
                break