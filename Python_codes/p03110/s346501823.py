import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    BB=380000
    ans =0
    N =int(input())

    for i in range(N):
        x,v =input().split()
        if v =="JPY":
            ans +=int(x)
        else:
            ans +=BB*float(x)

    print(ans)


if __name__ == "__main__":
    main()
