import itertools

def main():
    N = input()
    D = map(int, input().split())
    ans = 0
    for v in itertools.combinations(D, 2):
        ans += v[0] * v[1]
    print(ans)


if __name__ == '__main__':
    main()
