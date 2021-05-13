def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def solve(N, A):
    MAXA = max(A)
    prev = 0
    ans = 0
    for a in A:
        if prev < a:
            diff = a - prev
            ans += diff
        prev = a
    return ans


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
