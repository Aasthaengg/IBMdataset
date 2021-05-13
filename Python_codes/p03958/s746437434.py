import sys

input = sys.stdin.readline


def main():
    K, T = map(int, input().split())
    A = list(map(int, input().split()))

    prev_idx = -1
    ans = 0
    for _ in range(K):
        cur_idx = -1
        max_num = 0
        for i, a in enumerate(A):
            if i == prev_idx:
                continue
            if a > max_num:
                max_num = a
                cur_idx = i
        if max_num == 0:
            ans = A[prev_idx]
            break
        A[cur_idx] -= 1
        prev_idx = cur_idx

    print(ans)


if __name__ == "__main__":
    main()
