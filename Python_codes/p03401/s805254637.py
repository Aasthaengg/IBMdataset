import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]
    cost = 0
    pre = 0
    for a in A[1:]:
        cost += abs(a - pre)
        pre = a

    for i, a in enumerate(A):
        if i == 0 or i == N + 1: continue
        print(cost - abs(a - A[i - 1]) - abs(a - A[i + 1]) + abs(A[i + 1] - A[i - 1]))


if __name__ == "__main__":
    main()
