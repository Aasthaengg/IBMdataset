import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    h, w = list(map(int, input().strip().split()))
    a = []
    for i in range(h):
        a.append(list(map(int, input().strip().split())))
    ans = []
    for i in range(h):
        for j in range(w):
            if i == h-1 and j == w-1:
                continue
            if a[i][j] % 2 == 1:
                if j == w-1:
                    a[i+1][j] += 1
                    p = i+2
                    q = j+1
                else:
                    a[i][j+1] += 1
                    p = i+1
                    q = j+2
                a[i][j] -= 1
                ans.append((i+1, j+1, p, q))
    print(len(ans))
    for t in ans:
        print(*t)
if __name__ == '__main__':
    main()
