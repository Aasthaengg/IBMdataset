s = input()
n = len(s)

alp = [chr(i) for i in range(97, 97+26)]

if n < 26:
    for a in alp:
        if a not in s:
            print(s + a)
            exit()
else:
    i = 25
    while True:
        if i == 0:
            print('-1')
            exit()
        if s[i - 1] < s[i]:
            break
        i -= 1
    t = sorted(s[i-1:])
    idx = t.index(s[i-1]) + 1
    print(s[:i-1] + t[idx])
