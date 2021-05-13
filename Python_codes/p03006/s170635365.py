import sys
N = int(sys.stdin.readline().rstrip())

if N == 1:
    print(1)
    exit()

zahyo = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    zahyo.append((x, y))
zahyo.sort()

p_q = set()
for i in range(N - 1):
    for j in range(i + 1, N):
        p = zahyo[j][0] - zahyo[i][0]
        q = zahyo[j][1] - zahyo[i][1]
        p_q.add((p, q))

ans = float("inf")
for p, q in p_q:
    used = set()
    ans_tmp = 0
    for i in range(N):
        if i not in used:
            x_base = zahyo[i][0]
            y_base = zahyo[i][1]
            ans_tmp += 1
            for j, (x, y) in enumerate(zahyo[i + 1:], 1):
                if x - x_base == p and y - y_base == q:
                    used.add(i + j)
                    x_base = x
                    y_base = y
    ans = min(ans_tmp, ans)
print(ans)