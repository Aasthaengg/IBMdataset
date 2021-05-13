import sys

input = sys.stdin.readline
MOD = 1000000007

N  = input()[:-1]

if len(N)== 1:
    print(int(N))
elif len(N)  == 2:
    if N[-1] == '9':
        print(int(int(N)/10) + 9)
    else:
        print(int(int(N)/10)-1 + 9)

else:
    res = 0
    if N[0] == '9':
        check = True
        for i in range(0,len(N)):
            if N[i] != '9':
                check = False
        if check:
            res = 9*(len(N))
        else:
            res = 9*(len(N)-1)+8
    else:
        check = True
        for i in range(1,len(N)):
            if N[i] != '9':
                check = False
            if check:
                res = 9*(len(N)-1)+int(N[0])
            else:
                res = 9*(len(N)-1)+int(N[0])-1
    print(res)