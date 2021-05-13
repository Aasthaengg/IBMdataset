s = list(input())
if len(s) % 2 != 0:
    s.pop(-1)

l = len(s) // 2 - 1
while True:
    t = 0
    for i in range(l):
        if s[i] == s[l + i]:
            t += 1
    if t == l:
        print(t * 2)
        exit(0)
    else:
        l -= 1