def resolve():
    N = int(input())
    an = sorted([int(n) for n in input().split()], reverse=True)

    print(sum(an[::2]) - sum(an[1::2]))


if __name__ == '__main__':
    resolve()