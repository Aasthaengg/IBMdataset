def main(n, A):
    if A[0] != 0:
        return -1

    A.append(0)
    A = A[::-1]

    res = 0
    for x, y in zip(A[:-1], A[1:]):
        if x <= y:
            res += y
        elif x - 1 == y:
            pass
        else:
            return -1

    return res


if __name__ == "__main__":
    n = int(input())
    a = [int(input()) for _ in range(n)]
    ans = main(n, a)
    print(ans)
