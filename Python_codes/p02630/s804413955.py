# coding: utf-8
# Your code here!
import collections
N = int(input())
s = input().split()
b = [str(l) for l in s]
c = collections.Counter(b)

K = int(input())
t = [input().split() for i in range(K)]

d = int(0)
e = int(0)
ans = int(0)
ckey = []
cvalue = []
clen = int(len(c))

for i in c.keys():
    ckey.append(i)
for i in c.values():
    cvalue.append(i)
for i in range(clen):
    ans = ans + int(ckey[i]) * int(cvalue[i])
    
for i in range(K):
    if c.get(t[i][0]) != None:
        d = c.get(t[i][0])
        if c.get(t[i][1]) != None:
            e = c.get(t[i][1])
            ans = ans - int(t[i][0]) * int(d) + int(t[i][1]) * int(d)
            print(ans)
            c[t[i][1]] = int(d) + int(e)
            c[t[i][0]] = 0
        else:
            ans = ans - int(t[i][0]) * int(d) + int(t[i][1]) * int(d)
            print(ans)
            c[t[i][1]] = int(d)
            c[t[i][0]] = 0
    else:
        print(ans)