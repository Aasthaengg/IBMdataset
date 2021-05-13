import sys
input = sys.stdin.readline


def read():
    N, H = map(int, input().strip().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().strip().split())
        A.append(a)
        B.append(b)
    return N, H, A, B


def solve(N, H, A, B):
    # 刀を振り続ける->最後にまとめて投げる
    amax = max(A)
    B.sort(reverse=True)
    ans = 0
    for b in B:
        if amax >= b:
            break
        H -= b
        ans += 1
        if H <= 0:
            break
    if H > 0:
        ans += H // amax
        if H % amax > 0:
            ans += 1 
    return ans


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
