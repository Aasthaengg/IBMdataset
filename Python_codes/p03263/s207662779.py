import sys
from fractions import gcd
def input(): return sys.stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    cnt = 0
    manip = []
    for i in range(H):
        for j in range(W - 1):
            if A[i][j] % 2 != 0:
                cnt += 1
                manip.append((i, j, i, j + 1))
                A[i][j] -= 1
                A[i][j + 1] += 1
    
    for i in range(H - 1):
        if A[i][W - 1] % 2 != 0:
            cnt += 1
            manip.append((i, W - 1, i + 1, W - 1))
            A[i][W - 1] -= 1
            A[i + 1][W - 1] += 1
    
    print(cnt)
    for a, b, c, d in manip:
        print("{} {} {} {}".format(a + 1, b + 1, c + 1, d + 1))


                



if __name__ == "__main__":
    main()
