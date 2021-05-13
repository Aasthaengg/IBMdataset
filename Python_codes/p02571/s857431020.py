s = input()
t = input()

max_tmp = 0
out = 0


def comp(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    return cnt


for i in range(len(s) - len(t) + 1):
    max_tmp = comp(s[i:i + len(t)], t)
    out = max(out, max_tmp)

print(len(t) - out)