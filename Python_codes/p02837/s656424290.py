import sys
readline = sys.stdin.buffer.readline

N = int(readline())
A = [[] for _ in range(N)]

for i in range(N):
    count = int(readline())
    for j in range(count):
        x, y = map(int, readline().split())
        x -= 1
        A[i].append([x, y])


ans = 0
for i in range(2**N):
    pattern = [0] * N
    valid = True
    for j in range(N):
        if (i >> j) & 1:
            pattern[j] = 1

    # ビットが1になっている人の証言をみる
    for k in range(N):
        if pattern[k]:
            for x, y in A[k]:
                if pattern[x] != y:  # 矛盾があれば終了、このパターンはありえない。
                    valid = False
                    break
    if valid:
        ans = max(ans, sum(pattern))

print(ans)
