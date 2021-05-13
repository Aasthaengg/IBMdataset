s = input()
last = s[-1]
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
n = len(ascii_lowercase)

for moji in ascii_lowercase:
    if moji not in s:
        s += moji
        print(s)
        exit()

sl = list(s)
for i in range(len(s)-1, -1,-1):
    idx = ascii_lowercase.index(s[i])
    for j in range(idx,n):
        if ascii_lowercase[j] not in sl:
            sl[i] = ascii_lowercase[j]
            print(''.join(sl))
            exit()
    sl.pop()

if not sl:
    print(-1)