import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = [list(map(lambda x: int(x) - 1, readline().split())) for _ in range(n)]
q = list(range(n))
cnt = 0
while q:
    cnt += 1
    qq = set()
    while q:
        x = q.pop()
        if a[a[x][0]][0] == x:
            qq.add(x)
            qq.add(a[x][0])
    if qq:
        for x in qq:
            a[x].pop(0)
            if a[x]:
                q.append(x)
    else:
        print(-1)
        exit()
print(cnt)
