import sys
from bisect import bisect_left
def input(): return sys.stdin.readline().strip()


def main():
    """
    nをmax(A)にしていい理由が腑に落ちなかったので厳密証明。
    とはいえ証明は簡単で、M=max(A), m=(AのM以外の元), R=(M/2に一番近いAの元), r=(m/2に一番近いAの元)
    とすると
        comb(M, R) >= comb(M, r) >= comb(m, r)
    てだけでした。。。
    """
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N == 2:
        print(A[1], A[0])
        return
    idx = bisect_left(A, A[-1] // 2)
    a = A[idx]
    if idx > 0 and (A[idx] - A[-1] / 2) > (A[-1] // 2 - A[idx - 1]):
        a = A[idx - 1]
    print(A[-1], a)


if __name__ == "__main__":
    main()
