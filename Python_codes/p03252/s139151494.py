s = input()
t = input()

my_d = dict()

for i, ch in enumerate(s):
    if ch not in my_d:
        if t[i] in my_d.values():
            print('No')
            exit()
        else:
            my_d[ch] = t[i]
    else:
        if my_d[ch] != t[i]:
            print('No')
            exit()

print('Yes')