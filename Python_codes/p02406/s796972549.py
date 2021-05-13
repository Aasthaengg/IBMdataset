import sys

n = input()

tmp1 = 3

while tmp1 <= n:
    if tmp1 % 3 == 0:
        string =  ' ' + str(tmp1)
        sys.stdout.write(string )
    else:
        tmp2 = tmp1
        while tmp2 > 0:
            if tmp2 % 10 == 3:
                string = ' ' + str(tmp1)
                sys.stdout.write(string)
                break
            tmp2 /= 10
    tmp1 += 1
    
print ""