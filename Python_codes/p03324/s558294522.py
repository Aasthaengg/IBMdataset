def main():
    D, N = map(int, input().split())

    c = pow(100, D)

    x = 1
    cnt = 0
    while True:
        if x % 100 != 0:
            cnt += 1
            if cnt == N:
                break
        x += 1
    print(x * c)


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
# 
# sys.setrecursionlimit(10 ** 7)
# 
# (int(x)-1 for x in input().split())
# rstrip()
