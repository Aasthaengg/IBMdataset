def resolve():
    a, b, k = map(int, input().split())
    for i in range(k):
        if i % 2 == 0:
            if a % 2:
                a -= 1
            next_b = b + a // 2
            a //= 2
            b = next_b
        else:
            if b % 2:
                b -= 1
            next_a = a + b // 2
            b //= 2
            a = next_a
    print(a, b)


if __name__ == "__main__":
    resolve()
