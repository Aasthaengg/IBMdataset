
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    nab = [int(x) for x in input().rstrip().split(" ")]
    n = nab[0]
    a = nab[1]
    b = nab[2]

    kurikaesi = n // (a + b)
    amari = n % (a + b)

    ans = kurikaesi * a
    ans += amari if amari < a else a
    print(ans)

if __name__ == "__main__":
    resolve()
