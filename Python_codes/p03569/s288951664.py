import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = input()
cnt_1 = 0
cnt_2 = len(s) - 1
ans = 0
m = len(s)
end = m // 2
for i in range(cnt_2 + 1):
    if s[cnt_1] == s[cnt_2]:
        if end != cnt_1:
            cnt_1 += 1
        if end != cnt_2:
            cnt_2 -= 1
    elif s[cnt_1] == 'x':
        cnt_1 += 1
        ans += 1
        m += 1
    elif s[cnt_2] == 'x':
        cnt_2 -= 1
        ans += 1
        m -= 1
    else:
        print(-1)
        exit()
    end = m // 2
    if end == cnt_1 and end == cnt_2:
        break
print(ans)
