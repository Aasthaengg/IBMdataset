mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i&1:
            cnt = 0
            for d in range(1, i+1):
                if i%d==0:
                    cnt += 1
            if cnt == 8:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
