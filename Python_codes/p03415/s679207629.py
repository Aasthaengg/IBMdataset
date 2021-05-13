import sys
## io
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))
## dp
INIT_VAL = 0
DP2 = lambda d1, d2: [[INIT_VAL]*d2 for _ in range(d1)]
DP3 = lambda d1, d2, d3: [[[INIT_VAL]*d3 for _ in range(d2)] for _ in range(d1)]

def main():
    res = ''
    for i in range(3): res += IS()[i]
    print(res)

if __name__ == '__main__':
    main()
