s = input()
for i in range(int(input())):
    q = input().split()
    op, a, b = q[0], int(q[1]), int(q[2])
    if op == 'print':
        print(s[a : b+1])
    elif op == 'reverse':
        t = s[a : b+1]
        s = s[:a] + t[::-1] + s[b+1:]
    elif op == 'replace':
        s = s[:a] + q[3] + s[b+1:]