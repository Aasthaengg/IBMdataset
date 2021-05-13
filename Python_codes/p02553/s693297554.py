
def resolve():
    a, b, c, d = map(int, input().split())

    res1 = a * c
    res2 = a * d
    res3 = b * c
    res4 = b * d

    print(max(res1, res2, res3, res4))


if __name__ == "__main__":
    resolve()