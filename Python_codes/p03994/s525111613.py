# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_c

s = input()
k = int(input())
n = len(s)
ans = []
for i in range(n):
    t = (ord('z') - ord(s[i]) + 1) % 26
    if k - t >= 0:
        ans.append('a')
        k -= t
    else:
        ans.append(s[i])
if k > 0:
    k %= 26
    ans[-1] = chr(ord(ans[-1]) + k)
print(''.join(ans))