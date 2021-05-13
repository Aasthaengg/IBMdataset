
def is_triangle(a, b, c):
    if a >= b + c:
        return False

    if b >= a + c:
        return False

    if c >= a + b:
        return False

    return True


def main():
    N = int(input())
    L = list([int(x) for x in input().split()])

    L.sort()

    count = 0
    for index, a in enumerate(L):
        if index + 2 == N:
            break

        for b_i in range(index+1, N):
            b = L[b_i]
            c = 1

            while not is_triangle(a, b, L[-c]):
                c += 1

            count += (N - b_i - c)

    print(count)


if __name__ == '__main__':
    main()
