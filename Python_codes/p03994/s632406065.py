# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_c
# 前の方からgreedyに`a`に変えていって、残った回数は最後の一文字で無限に回す?


def ord_until_a(char):
    if char == 'a':
        return 0
    return ord('a') + 26 - ord(char)
    # return 26 - (ord(char) - ord('a'))


S = input()
K = int(input())
ans = []
for s in S:
    diff = ord_until_a(s)
    if K >= diff:
        ans.append('a')
        K -= diff
    else:
        ans.append(s)

if K > 0:
    K %= 26
    last = ord(ans[-1]) + K
    if last > ord('z'):
        last -= 26
    ans[-1] = chr(last)

print(''.join(ans))
