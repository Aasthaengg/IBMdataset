import sys
n = int(input())
a_ls = [int(i) for i in sys.stdin.readline().split()]
b_ls = [int(i) for i in sys.stdin.readline().split()]
plus_ls = []
minus_ls = []
for a, b in zip(a_ls, b_ls):
    if b > a:
        minus_ls.append(b - a)
    elif a > b:
        plus_ls.append(a - b)
    else:
        pass
plus_ls.sort(reverse=True)
sum_min = sum(minus_ls)

cnt = len(minus_ls)
for i in plus_ls:
    if sum_min <= 0:
        break
    sum_min -= i
    cnt += 1
if sum_min > 0:
    print(-1)
else:
    print(cnt)