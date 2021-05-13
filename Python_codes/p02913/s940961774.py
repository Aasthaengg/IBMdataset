# import sys
# sys.setrecursionlimit
# getarr = lambda _f: list(map(_f, input().split()))

n = int(input())
s = input()

s += '_'

ans = 0
for i in range(1, n):
    tmp = 0
    for j in range(i, n + 1):
        if s[j - i] == s[j]:
            tmp += 1
            if tmp >= i:
                ans = i
                break
        else:
            ans = max(ans, tmp)
            tmp = 0

print(ans)
