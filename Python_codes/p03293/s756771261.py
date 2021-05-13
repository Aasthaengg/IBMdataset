S = list(input())
T = input()
l = len(S)
s = S
for i in range(l):
    li = []
    li.append(s[-1])
    li.extend(s[0:-1])
    moji = ''.join(li)
    if moji == T:
        print('Yes')
        exit()
    s = moji
print('No')