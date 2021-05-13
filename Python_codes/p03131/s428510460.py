import sys
input = sys.stdin.readline


def read():
    K, A, B = list(map(int, input().strip().split()))
    return K, A, B


def solve(K, A, B):
    ans = 1
    if B-A <= 1:
        ans += K
        return ans
    if K < A-1:
        ans += K
        return ans
    ans += (A-1)
    k = K-A+1
    ans += (B-A) * (k//2) + k % 2
    return ans


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
