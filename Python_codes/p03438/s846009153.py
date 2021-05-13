import sys
input = sys.stdin.readline


def main():
    n = int(input())
    A = [int(i) for i in input().strip().split()]
    B = [int(i) for i in input().strip().split()]

    _diff_A, _diff_B = 0, 0
    m = sum(B) - sum(A)  # 操作回数の上限
    for i in range(n):
        if A[i] > B[i]:
            _diff_A += A[i] - B[i]
        elif B[i] > A[i]:
            _diff_B += (B[i] - A[i] + 1) // 2

    if _diff_B <= m and _diff_A <= m:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
