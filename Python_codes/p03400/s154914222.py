def main():
    n = int(input())
    v = list(map(int, input().split()))
    d = v[0]
    x = v[1]
    a = []

    for i in range(n):
        a.append(int(input()))

    answer = 0

    for i in range(len(a)):
        eat = 0
        day = 1
        while day <= d:
            eat += 1
            day += a[i]
        answer += eat

    answer += x

    print(answer)


if __name__ == "__main__":
    main()
