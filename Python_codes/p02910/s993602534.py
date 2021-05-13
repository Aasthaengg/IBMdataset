# 問題：https://atcoder.jp/contests/abc141/tasks/abc141_b

s = input()
i = 1
res = True
for ch in s:
    if i % 2 == 1 and ch == 'L':
        res = False
        break
    elif i % 2 == 0 and ch == 'R':
        res = False
        break
    i += 1

if res:
    print('Yes')
else:
    print('No')
