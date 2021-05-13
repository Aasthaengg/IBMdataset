N, M = map(int, input().split())

M_MAX = (N - 1) // 2

pos = 1
size = M_MAX
i = 0
while i < M and size > 0:
    print(pos, pos + size)
    pos += 1
    i += 1
    size -= 2

pos = 1 + M_MAX + 1
size = M_MAX - 1
while i < M and size > 0:
    print(pos, pos + size)
    pos += 1
    i += 1
    size -= 2