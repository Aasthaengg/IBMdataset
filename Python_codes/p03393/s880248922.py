s = input()

if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

if len(s) < 26:
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            print(s+i)
            exit()

else:
    s = list(s)
    t = []
    for i in range(len(s)):
        t.append(s[-1-i])
        t.sort(reverse=True)
        if t != s[-1-i:]:
            l = s[-1-i]
            for j in range(ord(l)-ord("a")+1,26):
                if chr(j+ord("a")) in t:
                    l = [chr(j+ord("a"))]
                    break
            for j in range(i+1,len(s)):
                l.append(s[-1-j])
            print(*l[::-1],sep="")
            exit()
    print(chr(ord(s[0])+1))