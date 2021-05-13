def resolve():
    N = int(input())
    res = 0
    for _ in range(N):
        l, r = [int(x) for x in input().split()]
        res += r - l + 1
    return res

if __name__ == '__main__':
    print(resolve())
