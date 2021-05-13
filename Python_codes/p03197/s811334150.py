# https://atcoder.jp/contests/caddi2018/tasks/caddi2018_b

n = int(input())
odd = even = 0
for _ in range(n):
    apple = int(input())
    if apple % 2 == 0:
        even += 1
    else:
        odd += 1

if odd:
    print('first')
else:
    print('second')