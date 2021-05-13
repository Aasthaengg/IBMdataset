import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c, d, e, f = map(int, readline().split())
A = 100 * a
B = 100 * b
E = e / (100 + e)
ans = [0, 0]
check = 0
for i in range(f // A + 2):
    for j in range(f // B + 2):
        w = A * i + B * j
        for k in range(int((w * E) // c) + 2):
            for l in range(int((w * E) // d) + 2):
                if k == 0 and l == 0:
                    continue
                s = c * k + d * l
                n = s / (w + s)
                if w + s > f or n > E:
                    break
                if n > check:
                    ans = w + s, s
                    check = n
                    if check == E:
                        print(*ans)
                        exit()
if ans[0] == 0:
    print(100 * a, ans[1])
else:
    print(*ans)
