import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def evenodd(n):
    if n % 2 == 0:
        return [n // 2, n // 2]
    else:
        return [(n - 1) // 2, (n + 1) // 2]


s = readline().decode().rstrip()

s = s+'R'
ans = [0] * (len(s))
rcnt = 0
lcnt = 0
for i in range(len(s)):
    if s[i] == 'R':
        rcnt += 1
        if lcnt >= 1 and rcnt == 1:
            c = evenodd(lcnt)
            ans[i - lcnt - 1] += c[0]
            ans[i - lcnt] += c[1]
            lcnt = 0
    if s[i] == 'L':
        lcnt += 1
        if lcnt == 1 and rcnt >= 1:
            c = evenodd(rcnt)
            ans[i - 1] += c[1]
            ans[i] += c[0]
            rcnt = 0

print(*ans[:-1:])
