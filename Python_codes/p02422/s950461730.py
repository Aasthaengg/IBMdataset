s = list(input())
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'print':
        print(''.join(s[int(cmd[1]):int(cmd[2]) + 1]))
    elif cmd[0] == 'reverse':
        s[int(cmd[1]):int(cmd[2]) + 1] = s[int(cmd[1]):int(cmd[2]) + 1][::-1]
    elif cmd[0] == 'replace':
        s[int(cmd[1]):int(cmd[2]) + 1] = list(cmd[3])