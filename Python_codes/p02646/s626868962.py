from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    A, V = ril()
    B, W = ril()
    T = ri()
    print('YES' if abs(A - B) <= T * (V - W) else 'NO')

if __name__ == '__main__':
    main()
