s = list(input())
t = input()

for i in range(len(s) - len(t), -1, -1):
    for j in range(len(t)):
        if s[i+j] != t[j] and s[i+j] != '?':
            break
    else:
        for j in range(len(t)):
            s[i+j] = t[j]
        for j in range(len(s)):
            if s[j] == '?':
                s[j] = 'a'
        print(''.join(s))
        exit()

print('UNRESTORABLE')