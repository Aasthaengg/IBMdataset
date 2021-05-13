from re import match
s, t = input().replace('?', '.'), input()

for i in range(len(s) - len(t) + 1)[::-1]:
    if match(s[i:i + len(t)], t):
        key = s.replace(s[i:i + len(t)], t).replace('.', 'a')
        s = s.replace('.', 'a')
        print(s[:i] + t + s[i + len(t):])
        #print(key)
        break
else:
    print('UNRESTORABLE')
