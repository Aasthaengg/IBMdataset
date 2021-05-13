import sys

n = input()

for i in range(1,n+1):
    x = i
    y = i
    flag = 0
    if(x % 3 == 0):
        flag = 1
        sys.stdout.write(" ")
        sys.stdout.write(str(x))
        if(i+1 > n):
            break

    while(1):
        if flag == 1:
            break
        if(y % 10 == 3):
            sys.stdout.write(" ")
            sys.stdout.write(str(x))
            break
            if(i+1 > n):
                break
        y = y/10
        if(y == 0):
            break
print