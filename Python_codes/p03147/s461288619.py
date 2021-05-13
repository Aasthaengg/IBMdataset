import sys
import numpy as np

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    H = nl()
    ans = 0
    while not all([h == 0 for h in H]):
        if len(set(H)) == 1:
            ans += H[0]
            H = [0] * n
        else:
            h_max = max(H)
            prev = -10
            for i in range(n):
                if H[i] == h_max:
                    if prev != i - 1:
                        ans += 1
                    prev = i
                    H[i] -= 1
    print(ans)


if __name__ == '__main__':
    main()
