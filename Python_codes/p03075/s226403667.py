import sys
ri = lambda: int(sys.stdin.readline())
li = [ri() for _ in range(6)]
print(':(' if li[4] - li[0] > li[5] else 'Yay!')
