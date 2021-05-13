def out(c, n):
    for i in range(n):
        print(c, end='')

sx, sy, tx, ty = map(int, input().split())

out('U', ty - sy)
out('R', tx - sx)
out('D', ty - sy)
out('L', tx - sx)

out('L', 1)
out('U', ty - sy + 1)
out('R', tx - sx + 1)
out('D', 1)
out('R', 1)
out('D', ty - sy + 1)
out('L', tx - sx + 1)
out('U', 1)

print()
