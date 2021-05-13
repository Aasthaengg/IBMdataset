from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    a, b, k = ril()
    t = True
    for i in range(k):
        if t:
            if a % 2 == 1:
                a -= 1
            b += a // 2
            a //= 2
        else:
            if b % 2 == 1:
                b -= 1
            a += b // 2
            b //= 2
        t = not t
    print(a, b)

if __name__ == '__main__':
    main()
