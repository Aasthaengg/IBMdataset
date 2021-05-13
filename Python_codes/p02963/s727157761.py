N = 10 ** 9

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    S = Z()
    x = (S + N - 1)//N
    y = N * x - S
    print(0, 0, 1, N, x, y)
    return

if __name__ == '__main__':
    main()
