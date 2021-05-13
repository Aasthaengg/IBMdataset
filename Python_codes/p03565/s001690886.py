s = input()[::-1]
t = input()[::-1]
for i in range(len(s)):
    for j in range(len(t)):
        if i + j >= len(s):
            break
        if s[i+j] != '?' and s[i+j] != t[j]:
            break
    else:
        tmp = list(s)
        for j in range(len(t)):
            tmp[i+j] = t[j]
        ans = str.replace(''.join(tmp), '?', 'a')[::-1]
        print(ans)
        break
else:
    print('UNRESTORABLE')