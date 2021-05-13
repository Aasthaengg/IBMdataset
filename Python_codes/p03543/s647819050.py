ns = input()
tmp = None
cnt = 0
flg = False
for n in ns:
    if n == tmp:
        cnt += 1
    else:
        cnt = 1
        tmp = n
    if cnt == 3:
        flg = True
        break
print("Yes" if flg else "No")