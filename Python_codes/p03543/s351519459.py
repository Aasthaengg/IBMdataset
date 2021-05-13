n = str(input())
flag = False

if n[0] == n[1] == n[2] or n[1] == n[2] == n[3]:
    flag = True

if flag:
    print('Yes')
else:
    print('No')