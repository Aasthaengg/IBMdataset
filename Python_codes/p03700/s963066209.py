import sys,math
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,a,b = map(int,readline().split())
h = [int(readline()) for i in range(n)]

def is_ok(arg):
    chk = 0
    for i in h:
      chk += max(0,math.ceil((-arg*b+i)/(a-b)))
    return chk <= arg


def bisect_ok(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義
    ng = 最小の値-1 ok = 最大の値+1 で最小
    最大最小が逆の場合はng ok をひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(bisect_ok(0,10**9))
