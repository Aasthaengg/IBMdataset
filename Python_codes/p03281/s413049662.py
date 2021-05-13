
import sys
read = sys.stdin.read
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
    r = 0
    for i1 in range(1, n + 1, 2):
        ifac = factorization(i1)
        ifacn = [i[1] for i in ifac]
        ifacn.sort()
        if ifacn == [1, 3] or ifacn == [1, 1, 1]:
            r += 1
    print(r)

if __name__ == '__main__':
    main()
