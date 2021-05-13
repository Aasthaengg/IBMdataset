s = input()
n = int(input())
for _ in range(n):
    l = input().split()
    i_1 = int(l[1])
    i_2 = int(l[2]) + 1
    if l[0] == 'replace':
        s = s[:i_1] + l[3] + s[i_2:]
    elif l[0] == 'reverse':
        s = s[:i_1] + s[i_1:i_2][::-1] + s[i_2:]
    elif l[0] == 'print':
        print(s[i_1:i_2])

