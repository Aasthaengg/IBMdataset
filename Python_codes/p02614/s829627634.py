import numpy as np
h,w,k = map(int,input().split())
c = list(list(input()) for i in range(h))
c = np.array(c)
ans = 0
for i in range(2**h):
    for j in range(2**w):
        x = i
        y = j
        s = np.copy(c)
        n = 0
        while x > 0:
            if x % 2 == 1:
                for l in range(w):
                    s[n][l] = '0'
            x = x // 2
            n += 1
        m = 0
        while y > 0:
            if y % 2 == 1:
                for l in range(h):
                    s[l][m] = '0'
            y = y // 2
            m += 1
        p = np.count_nonzero(s == '#')
        if p == k:
            ans += 1
print(ans)