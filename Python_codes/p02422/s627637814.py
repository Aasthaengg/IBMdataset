# -*- coding: utf-8 -*-

s = str(raw_input())
q = int(raw_input())
for i in range(q):
    line = map(str, raw_input().split())
    com = line[0]
    a = int(line[1])
    b = int(line[2])
    if com == "print":
        print s[a:b+1]
    elif com == "reverse":
        tmp = s[::-1]
        s = s[:a] + tmp[len(tmp)-b-1:len(tmp)-a] + s[b+1:]
    elif com == "replace":
        p = line[3]
        s = s[:a] + p + s[b+1:]
    else:
        print "Error"