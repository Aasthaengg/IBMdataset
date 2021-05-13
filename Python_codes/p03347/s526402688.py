import sys

n = int(sys.stdin.readline().strip())
a_ls = []
for i in range(n):
    a = int(sys.stdin.readline().strip())
    a_ls.append(a)

if a_ls[0] != 0:
    print(-1)
else:
    cur = a_ls[-1]
    res = cur
    for a in a_ls[::-1][1:]:
        cur -= 1
        if a - cur > 0:
            res += a
            cur = a
        elif a == cur:
            continue
        else:
            res = -1
            break
    print(res)