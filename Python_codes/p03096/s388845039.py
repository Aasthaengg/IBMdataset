import sys

N = int(input())
C = []
pre = 0
for _ in range(N):
    c = int(sys.stdin.readline())
    if pre == c:
        continue
    else:
        C.append(c)
        pre = c

ans = 1
dic = {}
for c in C:
    if c in dic.keys():
        a = dic[c]
        dic[c] += ans
        ans += a
    else:
        dic[c] = ans

print(ans % (10 ** 9 + 7))
