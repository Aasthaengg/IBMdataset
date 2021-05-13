# -*- coding: utf-8 -*-
def call(n):
    for i in (range(1,n+1)):
        x = i
        if(x % 3 == 0):
            print(" {0}".format(i), end="")
        else:
            while(x):
                if(x % 10 == 3):
                    print(" {0}".format(i), end="")
                    break;
                x = int(x / 10)
    print()

input = int(input().strip())
call(input)