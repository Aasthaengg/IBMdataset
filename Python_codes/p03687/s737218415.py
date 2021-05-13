s = input()

def func(st,char):
    ans = [None] * (len(st) - 1)
    for i in range(len(ans)):
        if st[i] == c or st[i + 1] == c:
            ans[i] = c
        else:
            ans[i] = st[i]
    # print(ans)
    return ''.join(ans)
m = 10 ** 5
for i in range(26):
    work = s
    c = chr(ord('a') + i)
    # print(c)
    cnt = 0
    while len(set(list(work))) != 1:
        work = func(work, c)
        cnt += 1
        # print(s, len(set(list(s))))
    m = min(m, cnt)
print(m)

