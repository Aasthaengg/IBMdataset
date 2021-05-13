# -*- coding: utf-8 -*-

while True:
    line = map(str, raw_input().split())
    H = int(line[0])
    W = int(line[1])
    if H+W:
        for i in range(H):
            if i == 0 or i == (H-1):
                print "#"*W
            else:
                print "#" + "."*(W-2) +"#"
        print ""
    else:
        break