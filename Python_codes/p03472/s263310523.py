import sys
import math


def input():
    return sys.stdin.readline().strip()


def main():
    N, H = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    B.sort(reverse=True)
    attack = 0
    cnt = N
    for i in range(N):
        if B[i] < max_a:
            cnt = i
            break
        attack += B[i]
        if attack >= H:
            print(i + 1)
            return

    print(cnt + math.ceil((H - attack) / max_a))


if __name__ == "__main__":
    main()
