import numpy as np
L = 10**5


def main():
    is_prime = np.full(L+1, True, dtype=bool)
    is_prime[0:2] = False
    for i in range(2, int(np.sqrt(L))+1):
        if is_prime[i] == False:
            continue
        is_prime[i+i:L+1:i] = False
    # ここまで素数判定
    # ここから2017に似た数を判定
    is_like_2017 = np.full(L+1, False, dtype=bool)

    for i in range(2, L+1):
        if 2*i-1 > L:
            break
        if is_prime[i]:
            is_like_2017[2*i-1] = True

    is_like_2017[2] = False

    is_like_2017 = np.logical_and(is_prime, is_like_2017)
    accumulate = np.cumsum(is_like_2017)

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(accumulate[r]-accumulate[l-1])


if __name__ == "__main__":
    main()
