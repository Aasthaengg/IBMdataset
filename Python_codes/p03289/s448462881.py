s = input()
ls = len(s)

sc = s[2:-1]
big = 0

import collections
c = collections.Counter(sc)


if s[0]=="A":
    if c["C"]==1:
        for i in range(ls):
            if s[i].isupper():
                big +=1
        if big ==2:
            print("AC")
            exit()

print("WA")