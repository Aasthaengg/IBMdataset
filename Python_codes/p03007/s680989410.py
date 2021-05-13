import sys
n = int(input())
a_ls = [int(i) for i in sys.stdin.readline().split()]
a_ls.sort()
flg = True
if a_ls[-1] < 0:
    score = - sum(a_ls) + a_ls[-1] * 2
    flg = False
elif a_ls[1] < 0:
    score = sum([abs(a) for a in a_ls])
else:
    score = sum(a_ls) - a_ls[0] * 2
cur = a_ls[0]
last = a_ls[-1]
print(score)
if flg:
    for i in range(1,n):
        a = a_ls[i]
        if a < 0:
            print(last, a)
            last -= a
            continue
        if i < n - 1:
            print(cur, a_ls[i])
            cur -= a_ls[i]
        else:
            print(last, cur)
else:
    for i in range(n-1):
        print(last, a_ls[i])
        last -= a_ls[i]