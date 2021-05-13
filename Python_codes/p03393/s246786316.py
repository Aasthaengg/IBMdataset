s = input()
l = "abcdefghijklmnopqrstuvwxyz"
flag = [False for i in range(26)]
for i in s:
    flag[l.index(i)] = True
if False in flag:
    print(s + l[flag.index(False)])
else:
    w = []
    for i in range(26):
        temp = s[-i - 1]
        w.append(temp)
        w.sort()
        if w[-1] == temp:
            continue
        else:
            print(s[:-i-1] + w[w.index(temp) + 1])
            break
    else:
        print(-1)