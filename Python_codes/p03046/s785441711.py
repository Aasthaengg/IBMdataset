def main():
    m, k = map(int, input().split())
    maximum = 2 ** m - 1

    if k==0:
        print(" ".join(map(str, range(0, maximum+1))), end=" ")
        print(" ".join(map(str, range(maximum, -1, -1))))
        return

    if m==1:
        print(-1)
        return

    if maximum < k:
        print(-1)
        return

    others = [i for i in range(1, maximum+1) if i!=k]
    print(0, k, 0, end=" ")
    print(" ".join(map(str, others)), k, " ".join(map(str, reversed(others))))


main()

