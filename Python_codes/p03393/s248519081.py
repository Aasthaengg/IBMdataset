s = input()
c = [0 for _ in range(26)]

for i in range(len(s)):
    c[ord(s[i])-97] = 1

if len(s) == 26:
    ind = len(s)-1

    for _ in range(len(s)):
        r = -1
        for i in range(ord(s[ind])-97+1, ord('z')-97+1):
            if c[i] == 0:
                r = i
                break

        if r != -1:
            print(s[:ind] + chr(r+97))
            exit()

        c[ord(s[ind])-97] = 0
        ind -= 1

    print(-1)

else:
    print(s + chr(c.index(0)+97))