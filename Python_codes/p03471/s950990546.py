import sys
a = -1
count = 0
if __name__ == '__main__':
    N, Y = map(int, input().split())
    for x in range(N + 1):
        for y in range(N + 1):
            z = N - x - y
            if z < 0:
                break
            if 10000*x + 5000*y + 1000*z == Y:
                print(x, y, z)
                sys.exit()
    print(a, a, a)