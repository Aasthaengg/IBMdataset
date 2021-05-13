def resolve():
    n, m, c = map(int, input().split())
    bn = list(map(int, input().split()))
    print(sum([1 for _ in range(n) if sum([a * b for a, b in zip(list(map(int, input().split())), bn)]) + c > 0]))


if __name__ == '__main__':
    resolve()