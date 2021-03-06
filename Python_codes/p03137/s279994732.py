import numpy as np

def main():
    N, M = map(int, input().split())
    if N >= M:
        print(0)
        exit()
    X = sorted(list(map(int, input().split())))
    if N == 1:
        print(X[-1] - X[0])
        exit()
    D = np.array([X[i+1] - X[i] for i in range(M-1)])
    idx_list = np.argsort(-D)[:N-1]
    ans = sum(D)
    for idx in idx_list:
        ans -= D[idx]
    print(ans)


if __name__ == '__main__':
    main()
