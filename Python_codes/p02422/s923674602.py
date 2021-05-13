s = input()
n = int(input())
for i in range(n):
    l = input().split()
    if l[0] == 'replace':
        s = s[:int(l[1])] + str(l[3]) + s[int(l[2]) + 1:]
    elif l[0] == 'reverse':
        s = s[:int(l[1])] + s[int(l[1]):int(l[2])+1][::-1] + s[int(l[2]) + 1:]
    elif l[0] == 'print':
        print(s[int(l[1]):int(l[2]) + 1])

