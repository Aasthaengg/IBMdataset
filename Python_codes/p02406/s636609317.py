import sys
def call(n):
    i = 1
    flg = 1
    while True:
        x = i
        if x % 3 == 0:
            sys.stdout.write(" "+str(i))
            flg = 0
        while flg == 1:
            if x % 10 == 3:
                sys.stdout.write(" "+str(i))
                flg = 0
            x /= 10
            if not x:
                flg = 0
        if i < n :
            i = i+1
            flg = 1
        else:
            sys.stdout.write("\n")
            break
n = input()
call(n)