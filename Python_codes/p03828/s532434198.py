from math import floor
large_p = 10**9 + 7
from operator import mul
from functools import reduce
def main():
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr

    n = int(input())
    n_sq = floor(n ** 0.5)
    divs = [1] * (n + 1)
    for i1 in range(n , 1, -1):
        div = factorization(i1)
        for dive, divnum in div:
            divs[dive] += divnum
    r = reduce(mul, divs)
    r %= large_p

    print(r)
if __name__ == '__main__':
    main()