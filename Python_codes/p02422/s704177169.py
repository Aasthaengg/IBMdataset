s = list(raw_input())
Q = input()
for q in range(Q):
    str_order = raw_input().split()
    a = int(str_order[1])
    b = int(str_order[2])
    if str_order[0] == 'print':
        print ''.join(s[a:b+1])
    elif str_order[0] == 'reverse':
        tmp = s[a:b+1]
        tmp.reverse()
        s[a:b+1] = tmp
    elif str_order[0] == 'replace':
        s[a:b+1] = list(str_order[3])