def main():
    n, k, q = map(int, input().split())
    a = []
    for i in range(q):
        a.append(int(input()))

    point = [0] * n

    for i in range(q):
        # point = list(map(lambda x: x - 1, point))
        point[a[i]-1] += 1

    for i in range(n):
        if k - (q - point[i]) > 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
