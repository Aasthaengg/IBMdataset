import numpy as np


def main():
    n = int(input())
    As = [list(map(int, input().split())) for _ in range(2)]
    cumsum0 = np.cumsum(As[0])
    cumsum1 = np.cumsum(As[1])

    ans = -float('inf')
    for i in range(n):
        ans_temp = cumsum0[i] + (cumsum1[n-1] - cumsum1[i]) + As[1][i]
        ans = max(ans, ans_temp)
    print(ans)


if __name__ == "__main__":
    main()
