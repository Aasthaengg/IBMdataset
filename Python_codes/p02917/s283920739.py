def read():
    N = int(input().strip())
    B = list(map(int, input().strip().split()))
    return N, B


def solve(N, B):
    ans = 0
    for i in range(N):
        if i == 0:
            a = B[i]
        elif i == N-1:
            a = B[i-1]
        else:
            a = min(B[i-1], B[i])
        ans += a
    return ans


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))