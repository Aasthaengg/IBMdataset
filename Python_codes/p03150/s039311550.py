# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b
import sys
s = input()
target = 'keyence'
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[:i] + s[j:]
        if sub == target:
            print('YES')
            sys.exit()
print('NO')

