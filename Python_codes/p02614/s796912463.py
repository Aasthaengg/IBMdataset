import sys
sys.setrecursionlimit(10**7)
from itertools import product
def input(): return sys.stdin.readline().rstrip()

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]

    ans = 0
    for row in product([0, 1], repeat=h):
        for col in product([0, 1], repeat=w):
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if row[i] and col[j] and c[i][j] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()