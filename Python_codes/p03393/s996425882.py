import string
s = input()

if s == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

lis =list(string.ascii_lowercase)
nlis = [0]*26

for i in s:
    t = lis.index(i)
    nlis[t] += 1

if sum(nlis) != 26:
    for i in range(26):
        if nlis[i] == 0:
            print(s+lis[i])
            break
else:
    for i in range(25, -1, -1):
        for j in lis:
            if s[i] < j and j not in s[:i]:
                print(s[:i] + j)
                exit()