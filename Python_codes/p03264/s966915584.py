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
    k = II()
    if k%2==0:
        print((k//2)**2)
    else:
        print(((k+1)//2)*(k//2))

if __name__ == '__main__':
    main()
