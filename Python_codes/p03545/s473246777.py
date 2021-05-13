s = list(input())
s = list(map(int, s))

ss = []

def numToString(s):
    if s >= 0:
        s = '+' + str(s)
    else:
        s = str(s)
    return s

for i in range(2):
    if sum(s) == 7:
        ss += str(s[0])
        ss += list(map(numToString, s[1:4]))
        ss = ''.join(ss)
        print(ss + '=7')
        exit()

    for j in range(2):
        if sum(s) == 7:
            ss += str(s[0])
            ss += list(map(numToString, s[1:4]))
            ss = ''.join(ss)
            print(ss + '=7')
            exit()

        for k in range(2):
            if sum(s) == 7:
                ss += str(s[0])
                ss += list(map(numToString, s[1:4]))
                ss = ''.join(ss)
                print(ss + '=7')
                exit()

            s[3] *= -1
        s[2] *= -1
    s[1] *= -1

