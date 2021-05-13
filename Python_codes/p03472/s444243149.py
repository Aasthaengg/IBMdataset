n, h = map(int, input().split())
a_ls = []
b_ls = []

for i in range(n):
    a, b = map(int, input().split())
    a_ls.append(a)
    b_ls.append(b)

a_ls.sort()
a_ls.reverse()

b_ls.sort()
b_ls.reverse()

tmp = 0
cnt = 0

for i in range(n):
    dmg = b_ls[i]
    if dmg < a_ls[0]:
        break
    else:
        cnt += 1
        tmp += dmg
        if tmp >= h:
            print(cnt)
            exit()

left = h - tmp

cnt += (left + a_ls[0] - 1) // a_ls[0]
print(cnt)
