import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    # 「素数の乗数」かつ「Nを割り切れる」数Zをなるべく多く選ぶ

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
    if n == 1:
        print(0)
        sys.exit()
    pfactors = factorization(n)
    r = 0
    for pfe in pfactors:
        pfe1 = pfe[1]
        t1 = 1
        while pfe1:
            if pfe1 >= t1:
                r += 1
                pfe1 -= t1
                t1 += 1
            else:
                break
    print(r)

if __name__ == '__main__':
    main()