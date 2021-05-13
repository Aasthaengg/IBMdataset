import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    h,w = map(int, input().split())
    S = [input() for _ in range(h)]
    ans = [[0]*(w+2) for _ in range(h)]
    ans.insert(0, [0]*(w+2))
    ans.append([0]*(w+2))

    for i in range(h):
        for j in range(w):
            if S[i][j] == '#':
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if k == l == 0:
                            ans[i+1][j+1] = '#'
                        if ans[i+k+1][j+l+1] != '#':
                            ans[i+k+1][j+l+1] += 1
    for i in range(1,h+1):
        tmp = ''
        for j in range(1,w+1):
            tmp += str(ans[i][j])
        print(tmp)


if __name__ == '__main__':
    main()
