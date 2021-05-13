# coding:utf-8
import sys
def call(n):
    i = 1
    sys.stdout.write(' ')
    while i <= n:
        x = i
        if x % 3 == 0:
            print i, 
            if i <= n:
                i += 1
                continue
        while x != 0:
            if x % 10 == 3:
                print i,
                if i <= n:
                    break
            x = int(x / 10)
        i += 1
    else:
        print
n = input()
call(n)

