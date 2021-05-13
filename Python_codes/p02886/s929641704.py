# B - TAKOYAKI FESTIVAL 2019
def main():
    import itertools

    n = int(input())
    d = list(map(int, input().split()))
    sum = 0

    for v in itertools.combinations(ｄ, 2):
        sum += v[0] * v[1]
    print(sum)

if __name__ == "__main__":
    main()