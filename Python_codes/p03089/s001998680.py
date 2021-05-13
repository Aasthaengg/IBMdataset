import sys
n = int(input())
b_ls = [int(i) for i in sys.stdin.readline().split()]
cnt = 0
res = []
while len(b_ls) > 0:
    flg = True
    for i in range(n - cnt - 1, -1, -1):
        if b_ls[i] == i + 1:
            cnt += 1
            res.append(i+1)
            b_ls.pop(i)
            flg = False
            break
    if flg:
        res = -1
        break
if res == -1:
    print(res)
else:
    for b in res[::-1]:
        print(b)