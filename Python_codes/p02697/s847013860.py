import sys
N, M = [int(x) for x in input().split()]

s = []; e = [];
s.append(1)
e.append(2 * -(-M // 2)) # 2 * ceiling(M/2)
s.append(N - 2 * (M // 2))
e.append(N)

n = 0
while True:
    for i in range(2):
        if n >= M: sys.exit()
        print(s[i], e[i])
        s[i] += 1
        e[i] -= 1
        n += 1