def main():
    v = list(map(int, input().split()))
    n = v[0]
    x = v[1]
    a = list(map(int, input().split()))

    # aの値が小さい順にぴったり配っていく
    count = 0
    a = sorted(a)

    for i in range(len(a)):
        if i == len(a) - 1:
            if x == a[i]:
                count += 1
        elif x >= a[i]:
            x -= a[i]
            count += 1
        else:
            break

    print(count)


if __name__ == "__main__":
    main()
