# -*- conding:utf-8 -*-


se = set()
n = int(input())
tmp = [input().split() for i in range(n)]


for i in tmp:
    cmd, v = i
    if cmd == "find":
        if v in se:
            print("yes")
        else:
            print ("no")
    else:
        se.add(v)