def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    a = Input()
    count = 0
    for i in range(1, n-1):
        if a[i] == sorted((a[i-1], a[i], a[i+1]))[1]:
            count += 1

    print(count)

main()