s = input()
ascii_lowercase = list('abcdefghijklmnopqrstuvwxyz')
s = list(s)
s = set(s)
s = list(s)
s = sorted(s)
n = len(s)
flag = 0

for i in range(n):
    if s[i] != ascii_lowercase[i]:
        print(ascii_lowercase[i])
        flag = 1
        break

if len(s) != len(ascii_lowercase) and flag != 1:
    print(ascii_lowercase[len(s)])
elif flag != 1:
    print('None')
