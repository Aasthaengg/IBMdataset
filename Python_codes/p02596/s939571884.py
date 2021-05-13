# coding: utf-8


def solve(*args: str) -> str:
    k = int(args[0])

    ret = 1
    a = 7 % k
    while(a):
        a = (a*10+7) % k
        ret += 1
        if k < ret:
            ret = -1
            break

    return str(ret)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
