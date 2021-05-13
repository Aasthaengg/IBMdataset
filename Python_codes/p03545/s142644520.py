import sys
if __name__ == '__main__':
    s = input()
    o = []
    n = len(s)
    
    for i in range(1 << n - 1):
        tmp = 0
        tmp += int(s[0])
        o.clear()
        for j in range(n - 1):
            if 1 << j & i == 0:
                tmp += int(s[j + 1])
                o.append('+')
            else:
                tmp -= int(s[j + 1])
                o.append('-')
        if tmp == 7:
            print(s[0]+o[0]+s[1]+o[1]+s[2]+o[2]+s[3]+'=7')
            sys.exit()