import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    a, b, x = map(int, input().split())
    if a <= x <= a + b:
        print('YES')
    else:
        print('NO')
resolve()