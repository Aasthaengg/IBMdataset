# coding: utf-8
# Here your code !

import fileinput

for line in fileinput.input():
    (hight,width) = map(int,line.split(" "))
    
    if hight == 0 and width == 0:
        break
    
    for a in range(hight):
        for b in range(width):
            print("#", end="")
        print("")
    print("")