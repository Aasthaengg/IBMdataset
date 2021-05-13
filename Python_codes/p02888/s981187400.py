
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

    L.sort(reverse=True)

    count = 0
    for a_i in range(N-2):
        b_i = a_i + 1
        c_i = 1
        while b_i + c_i < N:

            if not is_triangle(L[a_i], L[b_i], L[-c_i]):
                c_i += 1

            else:
                count += (N - b_i - c_i)
                b_i += 1

    print(count)


if __name__ == '__main__':
    main()
