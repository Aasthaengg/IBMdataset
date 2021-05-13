s = input()
n = int(input())
for i in range(n):
    tmp = input().split()
    if tmp[0] == 'print':
        a = int(tmp[1])
        b = int(tmp[2])
        print(s[a:b+1])
    elif tmp[0] == 'reverse':
        a = int(tmp[1])
        b = int(tmp[2])
        c = s[a:b+1]
        r = c[::-1]
        s = s[:a] + r + s[b+1:]
    elif tmp[0] == 'replace':
        a = int(tmp[1])
        b = int(tmp[2])
        p = tmp[3]
        s = s[:a] + p + s[b+1:]
