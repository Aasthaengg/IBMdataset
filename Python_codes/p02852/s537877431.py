#!/usr/bin/env python3
n, m = map(int, input().split())
s = input()
ans = []
cur = n
while cur:
    for d in range(1, min(cur + 1, m + 1))[::-1]:
        if s[cur - d] == '0':
            ans.append(d)
            cur -= d
            break
    else:
        print(-1)
        exit()
print(*ans[::-1], sep=' ')
