import sys

input = sys.stdin.readline


def g(n):
    if n == -1:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1

    b = bin(n)[2:]
    res = 0
    # xxxx10: 01, 10
    if b[-2:] == "10":
        res += 3
    # xxxx11: 01, 10, 11
    elif b[-2:] == "11":
        pass
    # xxxx00 or xxxx01
    else:
        res += int(b[-1])

    for i in range(len(b) - 2):
        if b[i] == "0":
            continue
        if b[-1] == "0":
            res += 1 << (len(b) - 1 - i)
    return res


def main():
    A, B = map(int, input().split())

    if A == B:
        ans = A
    else:
        ans = g(A - 1) ^ g(B)

    print(ans)


if __name__ == "__main__":
    main()
