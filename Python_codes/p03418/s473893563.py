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
    n, k = MII()
    cnt = 0
    for b in range(k+1, n+1):
        p = n//b
        r = n%b
        if k==0:
            cnt += p*(b-k)+max(0, (r-k))
        else:
            cnt += p*(b-k)+max(0, (r-k+1))
    print(cnt)

if __name__ == '__main__':
    main()
