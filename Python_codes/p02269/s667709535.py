import sys
n = int(sys.stdin.readline())

dic = {}
for i in range(n):
    s = sys.stdin.readline()
    if s[0] == 'i':
        dic[s[7:]] = 1
    else:
        if s[5:] in dic:
            print('yes')
        else:
            print('no')
