def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    x = list(range(1, n+1))
    p = Input()
    data = [i != j for i, j in zip(x, p)]
    if sum(data) > 2:
        print("NO")
    else:
        print("YES")

main()