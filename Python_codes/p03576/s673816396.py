from copy import deepcopy
import sys
def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    x, y = [], []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    X, Y = deepcopy(x), deepcopy(y)
    x.sort()
    y.sort()
    ans = (x[-1] - x[0]) * (y[-1] - y[0])
    for i in range(n):
        for j in range(i + 1, n):
            for K in range(n):
                for l in range(K + 1, n):
                    cnt = 0
                    x1, x2, y1, y2 = x[i], x[j], y[K], y[l]
                    for m in range(n):
                        if x1 <= X[m] <= x2 and y1 <= Y[m] <= y2:
                            cnt += 1
                    if cnt >= k:
                        ans = min(ans, (x2 - x1) * (y2 - y1))
    print(ans)
if __name__ == "__main__":
    main()