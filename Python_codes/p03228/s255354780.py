a, b, k = map(int, input().split())


def calc(n):
    if n % 2 == 1:
        return n - 1
    else:
        return n


if __name__ == '__main__':
    for i in range(k):
        if i % 2 == 0:
            a = calc(a)
            b += a//2
            a //= 2
        else:
            b = calc(b)
            a += b//2
            b //= 2
print(a, b)
