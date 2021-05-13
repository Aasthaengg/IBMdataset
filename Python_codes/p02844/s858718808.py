#!/usr/bin/env python3
n = int(input())
s = input()

c = 0

for i in range(10):
    i = str(i)
    for j in range(10):
        j = str(j)
        for k in range(10):
            k = str(k)
            if i in s:
                t = s[s.index(i)+1:]
                if j in t:
                    u = t[t.index(j)+1:]
                    if k in u:
                        c+=1
print(c)
