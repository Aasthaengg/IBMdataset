s=input()
if s=="zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    quit()
elif len(s)<26:
    d=set([i for i in range(26)])
    for i in s:
        d.remove(ord(i)-97)
    print(s+chr(min(d)+97))
else:
    d=[ord(s[-1])]
    for i in range(25):
        c=s[-2-i]
        if max(d)<ord(c):
            d.append(ord(c))
        else:
            print(s[:26-2-i]+chr(min([i for i in d if i>ord(c)])))
            break