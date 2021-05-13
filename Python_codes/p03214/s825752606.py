def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    ave = sum(a) / n
    diffs = sorted([(abs(ai - ave), i) for i, ai in enumerate(a)])[0][1]
    print(diffs)


if __name__ == "__main__":
    resolve()
